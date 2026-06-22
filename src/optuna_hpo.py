from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

from dotenv import load_dotenv

try:
    import optuna
except ImportError as exc:
    raise SystemExit(
        "Optuna is not installed. Install dependencies first, e.g. `pip install optuna` "
        "or update the venv from requirements.txt."
    ) from exc


REPO_ROOT = Path(__file__).resolve().parent.parent


def env_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


def env_int(name: str, default: int) -> int:
    return int(os.getenv(name, str(default)))


def env_float(name: str, default: float) -> float:
    return float(os.getenv(name, str(default)))


def env_choices(name: str, default: str) -> list[str]:
    value = os.getenv(name, default)
    return [part.strip() for part in value.split(",") if part.strip()]


def load_hpo_env() -> None:
    load_dotenv(REPO_ROOT / ".env")
    hpo_env_path = Path(os.getenv("HPO_ENV_FILE", str(REPO_ROOT / "optuna_hpo.env")))
    if hpo_env_path.is_file():
        load_dotenv(hpo_env_path, override=True)


def suggest_trial_env(trial: optuna.Trial) -> dict[str, str]:
    batch_choices = [int(value) for value in env_choices("HPO_BATCH_SIZE_CHOICES", "16,24,32,48")]
    hidden_choices = [int(value) for value in env_choices("HPO_HIDDEN_DIM_CHOICES", "384,512,640")]
    block_choices = [int(value) for value in env_choices("HPO_NUM_BLOCKS_CHOICES", "4,6,8")]
    dilation_choices = [int(value) for value in env_choices("HPO_DILATION_FACTOR_CHOICES", "1,2,3")]

    batch_size = trial.suggest_categorical("batch_size", batch_choices)
    hidden_dim = trial.suggest_categorical("hidden_dim", hidden_choices)
    num_blocks = trial.suggest_categorical("num_blocks", block_choices)
    dilation_factor = trial.suggest_categorical("dilation_factor", dilation_choices)
    base_lr = trial.suggest_float(
        "base_lr",
        env_float("HPO_BASE_LR_LOW", 1e-5),
        env_float("HPO_BASE_LR_HIGH", 2e-4),
        log=True,
    )
    weight_decay = trial.suggest_float(
        "weight_decay",
        env_float("HPO_WEIGHT_DECAY_LOW", 1e-4),
        env_float("HPO_WEIGHT_DECAY_HIGH", 5e-2),
        log=True,
    )

    return {
        "BATCH_SIZE": str(batch_size),
        "ACCUMULATION_STEPS": os.getenv("HPO_ACCUMULATION_STEPS", "1"),
        "HIDDEN_DIM": str(hidden_dim),
        "NUM_BLOCKS": str(num_blocks),
        "DILATION_FACTOR": str(dilation_factor),
        "BASE_LR": str(base_lr),
        "WEIGHT_DECAY": str(weight_decay),
    }


def fixed_trial_env(trial_number: int, trial_dir: Path) -> dict[str, str]:
    env = {
        "MAX_STEPS": os.getenv("HPO_MAX_STEPS", "3000"),
        "VAL_CHECK_INTERVAL": os.getenv("HPO_VAL_CHECK_INTERVAL", "1000"),
        "LIMIT_VAL_BATCHES": os.getenv("HPO_LIMIT_VAL_BATCHES", "64"),
        "MAX_VAL_SAMPLES": os.getenv("HPO_MAX_VAL_SAMPLES", "2048"),
        "NUM_SANITY_VAL_STEPS": "0",
        "SAMPLE_LOG_EVERY_N_STEPS": os.getenv("HPO_SAMPLE_LOG_EVERY_N_STEPS", "999999999"),
        "CONSOLE_LOG_EVERY_N_BATCHES": os.getenv("HPO_CONSOLE_LOG_EVERY_N_BATCHES", "500"),
        "CHECKPOINT_EVERY_N_STEPS": os.getenv("HPO_CHECKPOINT_EVERY_N_STEPS", "1000"),
        "COMET_UPLOAD_CHECKPOINTS": "0",
        "CHECKPOINT_DIR": str(trial_dir / "checkpoints"),
        "TRAIN_RESULT_JSON": str(trial_dir / "result.json"),
    }

    for name in [
        "DATASET_FRACTION",
        "MAX_PROMPT_LEN",
        "MAX_CODE_LEN",
        "NUM_WORKERS",
        "PREFETCH_FACTOR",
        "CACHE_CHUNK_SIZE",
        "ENCODE_BATCH_SIZE",
    ]:
        if os.getenv(name) is not None:
            env[name] = os.getenv(name, "")

    if env_bool("HPO_DISABLE_COMET", True):
        env["COMET_API_KEY"] = ""

    env["HPO_TRIAL_NUMBER"] = str(trial_number)
    return env


def run_trial_subprocess(trial: optuna.Trial) -> dict:
    trials_root = Path(os.getenv("HPO_TRIALS_DIR", str(REPO_ROOT / "hpo_trials")))
    trial_dir = trials_root / f"trial_{trial.number:04d}"
    trial_dir.mkdir(parents=True, exist_ok=True)

    env = os.environ.copy()
    env.update(fixed_trial_env(trial.number, trial_dir))
    env.update(suggest_trial_env(trial))

    (trial_dir / "env.json").write_text(
        json.dumps({key: env[key] for key in sorted(env) if key.startswith(("HPO_", "MAX_", "VAL_", "LIMIT_", "BATCH_", "ACCUMULATION_", "HIDDEN_", "NUM_", "DILATION_", "BASE_", "WEIGHT_", "CHECKPOINT_", "TRAIN_", "COMET_", "DATASET_"))}, indent=2),
        encoding="utf-8",
    )

    command = [sys.executable, str(REPO_ROOT / "src" / "train.py")]
    timeout = env_int("HPO_TRIAL_TIMEOUT_SECONDS", 0)
    stdout_path = trial_dir / "stdout.log"
    stderr_path = trial_dir / "stderr.log"

    with stdout_path.open("w", encoding="utf-8") as stdout, stderr_path.open("w", encoding="utf-8") as stderr:
        completed = subprocess.run(
            command,
            cwd=REPO_ROOT,
            env=env,
            stdout=stdout,
            stderr=stderr,
            timeout=None if timeout <= 0 else timeout,
            check=False,
            text=True,
        )

    trial.set_user_attr("trial_dir", str(trial_dir))
    trial.set_user_attr("stdout", str(stdout_path))
    trial.set_user_attr("stderr", str(stderr_path))

    if completed.returncode != 0:
        tail = stderr_path.read_text(encoding="utf-8", errors="replace")[-4000:]
        trial.set_user_attr("failure_stderr_tail", tail)
        raise RuntimeError(f"Training subprocess failed with exit code {completed.returncode}. See {stderr_path}")

    result_path = trial_dir / "result.json"
    if not result_path.is_file():
        raise RuntimeError(f"Training finished but did not write {result_path}.")

    result = json.loads(result_path.read_text(encoding="utf-8"))
    trial.set_user_attr("best_model_path", result.get("best_model_path"))
    trial.set_user_attr("global_step", result.get("global_step"))
    trial.set_user_attr("train_rows", result.get("train_rows"))
    trial.set_user_attr("val_rows", result.get("val_rows"))
    return result


def objective(trial: optuna.Trial) -> float:
    result = run_trial_subprocess(trial)
    best_val_loss = result.get("best_val_loss")
    if best_val_loss is None:
        raise RuntimeError("Training result did not contain best_val_loss.")
    trial.report(float(best_val_loss), step=int(result.get("global_step") or 0))
    return float(best_val_loss)


def main() -> None:
    load_hpo_env()

    storage = os.getenv("HPO_STORAGE", f"sqlite:///{REPO_ROOT / 'optuna_hpo.db'}")
    study_name = os.getenv("HPO_STUDY_NAME", "diffcoder_hpo")
    seed = env_int("HPO_SEED", 42)

    sampler = optuna.samplers.TPESampler(seed=seed)
    pruner = optuna.pruners.MedianPruner(
        n_startup_trials=env_int("HPO_PRUNER_STARTUP_TRIALS", 5),
        n_warmup_steps=env_int("HPO_PRUNER_WARMUP_STEPS", 0),
    )
    study = optuna.create_study(
        study_name=study_name,
        storage=storage,
        direction="minimize",
        load_if_exists=True,
        sampler=sampler,
        pruner=pruner,
    )

    study.optimize(
        objective,
        n_trials=env_int("HPO_N_TRIALS", 20),
        timeout=None if env_int("HPO_TIMEOUT_SECONDS", 0) <= 0 else env_int("HPO_TIMEOUT_SECONDS", 0),
        gc_after_trial=True,
    )

    print(f"Best value: {study.best_value}")
    print(f"Best params: {study.best_params}")
    print(f"Best trial dir: {study.best_trial.user_attrs.get('trial_dir')}")


if __name__ == "__main__":
    main()
