from __future__ import annotations

import json
import os
import subprocess
import sys
import hashlib
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

try:
    import optuna
except ImportError as exc:
    raise SystemExit(
        "Optuna is not installed. Install dependencies first, e.g. `pip install optuna` "
        "or update the venv from requirements.txt."
    ) from exc

try:
    from optuna_integration.comet import CometCallback
except ImportError:
    try:
        from optuna_integration import CometCallback
    except ImportError:
        CometCallback = None


REPO_ROOT = Path(__file__).resolve().parent.parent
COMET_PARAM_PREFIXES = (
    "HPO_",
    "MAX_",
    "VAL_",
    "LIMIT_",
    "BATCH_",
    "ACCUMULATION_",
    "HIDDEN_",
    "NUM_",
    "DILATION_",
    "BASE_",
    "MIN_LR",
    "LR_",
    "WEIGHT_",
    "DATASET_",
    "MASK_",
    "TOPOLOGY_",
    "GENERATION_",
    "VAL_AST_",
)


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


def search_space_namespace(parts: dict[str, list[int]]) -> str:
    configured = os.getenv("HPO_SEARCH_SPACE_NAMESPACE")
    if configured:
        return configured

    payload = json.dumps(parts, sort_keys=True)
    digest = hashlib.sha1(payload.encode("utf-8")).hexdigest()[:8]
    return f"space_{digest}"


def suggest_categorical_in_namespace(
    trial: optuna.Trial,
    name: str,
    choices: list[int],
    namespace: str,
) -> int:
    value = trial.suggest_categorical(f"{name}_{namespace}", choices)
    trial.set_user_attr(name, value)
    return int(value)


def load_hpo_env() -> None:
    load_dotenv(REPO_ROOT / ".env")
    hpo_env_path = Path(os.getenv("HPO_ENV_FILE", str(REPO_ROOT / "optuna_hpo.env")))
    if hpo_env_path.is_file():
        load_dotenv(hpo_env_path, override=True)


def hpo_comet_enabled() -> bool:
    return env_bool("HPO_LOG_COMET", bool(os.getenv("COMET_API_KEY")))


def hpo_manual_comet_enabled() -> bool:
    return env_bool("HPO_LOG_COMET_MANUAL", False)


def safe_comet_call(experiment, method_name: str, *args, **kwargs) -> None:
    if experiment is None:
        return
    try:
        method = getattr(experiment, method_name, None)
        if method is not None:
            method(*args, **kwargs)
    except Exception as exc:
        print(f"[HPO COMET WARNING] {method_name} failed: {exc}", file=sys.stderr)


def create_hpo_comet_experiment(trial: optuna.Trial, trial_dir: Path):
    if not hpo_manual_comet_enabled():
        return None

    try:
        from comet_ml import Experiment
    except ImportError:
        print("[HPO COMET WARNING] comet_ml is not installed; HPO trial logging disabled.", file=sys.stderr)
        return None

    api_key = os.getenv("COMET_API_KEY")
    if not api_key:
        print("[HPO COMET WARNING] COMET_API_KEY is missing; HPO trial logging disabled.", file=sys.stderr)
        return None

    project_name = os.getenv("HPO_COMET_PROJECT_NAME") or os.getenv("COMET_PROJECT_NAME") or "diffcoder-hpo"
    workspace = os.getenv("HPO_COMET_WORKSPACE") or os.getenv("COMET_WORKSPACE")
    try:
        experiment = Experiment(
            api_key=api_key,
            project_name=project_name,
            workspace=workspace,
            auto_param_logging=False,
            auto_metric_logging=False,
            auto_output_logging="simple",
        )
    except TypeError:
        experiment = Experiment(api_key=api_key, project_name=project_name, workspace=workspace)
    except Exception as exc:
        print(f"[HPO COMET WARNING] Could not create experiment: {exc}", file=sys.stderr)
        return None

    study_name = os.getenv("HPO_STUDY_NAME", "diffcoder_hpo")
    started_at = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    safe_comet_call(experiment, "set_name", f"{study_name}-trial-{trial.number:04d}-{started_at}")
    safe_comet_call(experiment, "add_tag", "optuna")
    safe_comet_call(experiment, "add_tag", "hpo")
    safe_comet_call(experiment, "add_tag", study_name)
    safe_comet_call(experiment, "log_other", "trial_dir", str(trial_dir))
    safe_comet_call(experiment, "log_other", "trial_number", trial.number)
    safe_comet_call(experiment, "log_other", "study_name", study_name)
    safe_comet_call(experiment, "log_metric", "trial_started", 1, step=0)
    return experiment


def log_hpo_trial_start(experiment, trial: optuna.Trial, env: dict[str, str], trial_dir: Path) -> None:
    if experiment is None:
        return

    sampled_params = {f"sampled_{key}": value for key, value in trial.params.items()}
    fixed_params = {
        key.lower(): value
        for key, value in env.items()
        if key.startswith(COMET_PARAM_PREFIXES)
        and key not in {"COMET_API_KEY", "COMET_WORKSPACE"}
    }
    safe_comet_call(experiment, "log_parameters", sampled_params)
    safe_comet_call(experiment, "log_parameters", fixed_params)

    env_path = trial_dir / "env.json"
    if env_path.is_file():
        safe_comet_call(experiment, "log_text", env_path.read_text(encoding="utf-8"), step=0)


def log_hpo_trial_success(experiment, result: dict, trial_dir: Path) -> None:
    if experiment is None:
        return

    global_step = int(result.get("global_step") or 0)
    for metric_name in ["best_monitor_score", "final_checkpoint_monitor", "final_val_loss", "final_train_loss"]:
        value = result.get(metric_name)
        if value is not None:
            safe_comet_call(experiment, "log_metric", metric_name, float(value), step=global_step)
    if result.get("best_monitor") is not None:
        safe_comet_call(experiment, "log_other", "best_monitor", result.get("best_monitor"))

    safe_comet_call(experiment, "log_metric", "trial_completed", 1, step=global_step)
    safe_comet_call(experiment, "log_other", "best_model_path", result.get("best_model_path"))
    safe_comet_call(experiment, "log_other", "last_model_path", result.get("last_model_path"))
    safe_comet_call(experiment, "log_text", json.dumps(result, ensure_ascii=True, indent=2), step=global_step)
    log_hpo_trial_log_tails(experiment, trial_dir, step=global_step)


def log_hpo_trial_failure(experiment, trial_dir: Path, reason: str, step: int = 0) -> None:
    if experiment is None:
        return

    safe_comet_call(experiment, "log_metric", "trial_failed", 1, step=step)
    safe_comet_call(experiment, "log_other", "failure_reason", reason)
    log_hpo_trial_log_tails(experiment, trial_dir, step=step)


def log_hpo_trial_log_tails(experiment, trial_dir: Path, step: int = 0) -> None:
    if experiment is None:
        return

    tail_chars = env_int("HPO_COMET_LOG_TAIL_CHARS", 8000)
    if tail_chars <= 0:
        return

    for name in ["stdout.log", "stderr.log"]:
        path = trial_dir / name
        if path.is_file():
            text = path.read_text(encoding="utf-8", errors="replace")[-tail_chars:]
            safe_comet_call(experiment, "log_text", f"--- {name} tail ---\n{text}", step=step)


def suggest_trial_env(trial: optuna.Trial) -> dict[str, str]:
    batch_choices = [int(value) for value in env_choices("HPO_BATCH_SIZE_CHOICES", "8,12,16,24")]
    hidden_choices = [int(value) for value in env_choices("HPO_HIDDEN_DIM_CHOICES", "256,384,512")]
    block_choices = [int(value) for value in env_choices("HPO_NUM_BLOCKS_CHOICES", "4,6")]
    dilation_choices = [int(value) for value in env_choices("HPO_DILATION_FACTOR_CHOICES", "1,2")]
    categorical_space = {
        "batch_size": batch_choices,
        "hidden_dim": hidden_choices,
        "num_blocks": block_choices,
        "dilation_factor": dilation_choices,
    }
    namespace = search_space_namespace(categorical_space)
    trial.set_user_attr("search_space_namespace", namespace)

    batch_size = suggest_categorical_in_namespace(trial, "batch_size", batch_choices, namespace)
    hidden_dim = suggest_categorical_in_namespace(trial, "hidden_dim", hidden_choices, namespace)
    num_blocks = suggest_categorical_in_namespace(trial, "num_blocks", block_choices, namespace)
    dilation_factor = suggest_categorical_in_namespace(trial, "dilation_factor", dilation_choices, namespace)
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
        "MASK_LOW_RANGE",
        "MASK_MIDDLE_RANGE",
        "MASK_HIGH_RANGE",
        "MASK_LOW_WEIGHT",
        "MASK_MIDDLE_WEIGHT",
        "MASK_HIGH_WEIGHT",
        "MASK_ALL_WEIGHT",
        "MASK_LOW_ALPHA",
        "MASK_MIDDLE_ALPHA",
        "MASK_HIGH_ALPHA",
        "MASK_LOW_BETA",
        "MASK_MIDDLE_BETA",
        "MASK_HIGH_BETA",
        "MASK_SAMPLER_SEED",
        "TOPOLOGY_INDEPENDENT_WEIGHT",
        "TOPOLOGY_BLOCK_WEIGHT",
        "TOPOLOGY_PREFIX_WEIGHT",
        "TOPOLOGY_TRUNCATED_SUFFIX_WEIGHT",
        "TOPOLOGY_BLOCK_LENGTHS",
        "TOPOLOGY_MIN_VISIBLE_PREFIX_FRACTION",
        "TOPOLOGY_MAX_VISIBLE_PREFIX_FRACTION",
        "TOPOLOGY_MIN_TRUNCATED_VISIBLE_TOKENS",
        "VAL_FIXED_MASK_BINS",
        "VAL_DETERMINISTIC_SEED",
        "VAL_LOGIT_CHUNK_SIZE",
        "VAL_FIXED_PROMPT_SAMPLES",
        "VAL_FIXED_PROMPT_EVERY_N_EPOCHS",
        "VAL_FIXED_GENERATION_CODE_LEN",
        "VAL_AST_EVAL_SAMPLES",
        "VAL_AST_GENERATION_STEPS",
        "VAL_AST_EVERY_N_STEPS",
        "VAL_AST_LOG_FAILURES",
        "VAL_PROMPT_SHUFFLE_DIAGNOSTIC",
        "VAL_PROMPT_SHUFFLE_MASK_PROB",
        "MIN_LR",
        "LR_WARMUP_STEPS",
        "CHECKPOINT_MONITOR",
        "CHECKPOINT_MODE",
        "GENERATION_DECODING_STRATEGY",
        "GENERATION_REMASK_CONFIDENCE_THRESHOLD",
        "GENERATION_MAX_REMASK_FRACTION_PER_STEP",
        "GENERATION_MAX_REMASKS_PER_TOKEN",
        "GENERATION_REMASK_COOLDOWN_STEPS",
        "GENERATION_DISABLE_REMASKING_LAST_N_STEPS",
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
    comet_experiment = create_hpo_comet_experiment(trial, trial_dir)

    env = os.environ.copy()
    env.update(fixed_trial_env(trial.number, trial_dir))
    env.update(suggest_trial_env(trial))

    (trial_dir / "env.json").write_text(
        json.dumps({key: env[key] for key in sorted(env) if key.startswith(("HPO_", "MAX_", "VAL_", "LIMIT_", "BATCH_", "ACCUMULATION_", "HIDDEN_", "NUM_", "DILATION_", "BASE_", "MIN_LR", "LR_", "WEIGHT_", "CHECKPOINT_", "TRAIN_", "COMET_", "DATASET_", "MASK_", "TOPOLOGY_", "GENERATION_"))}, indent=2),
        encoding="utf-8",
    )
    log_hpo_trial_start(comet_experiment, trial, env, trial_dir)

    command = [sys.executable, str(REPO_ROOT / "src" / "train.py")]
    timeout = env_int("HPO_TRIAL_TIMEOUT_SECONDS", 0)
    stdout_path = trial_dir / "stdout.log"
    stderr_path = trial_dir / "stderr.log"

    try:
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
    except subprocess.TimeoutExpired as exc:
        trial.set_user_attr("trial_dir", str(trial_dir))
        trial.set_user_attr("stdout", str(stdout_path))
        trial.set_user_attr("stderr", str(stderr_path))
        trial.set_user_attr("failure_reason", "timeout")
        log_hpo_trial_failure(comet_experiment, trial_dir, "timeout")
        safe_comet_call(comet_experiment, "end")
        raise RuntimeError(f"Training subprocess timed out after {exc.timeout}s. See {stderr_path}") from exc

    trial.set_user_attr("trial_dir", str(trial_dir))
    trial.set_user_attr("stdout", str(stdout_path))
    trial.set_user_attr("stderr", str(stderr_path))

    if completed.returncode != 0:
        tail = stderr_path.read_text(encoding="utf-8", errors="replace")[-4000:]
        trial.set_user_attr("failure_stderr_tail", tail)
        lower_tail = tail.lower()
        resource_markers = [
            "cuda out of memory",
            "outofmemoryerror",
            "cublas_status_alloc_failed",
            "cudnn_status_alloc_failed",
            "defaultcpuallocator",
            "not enough memory",
        ]
        if any(marker in lower_tail for marker in resource_markers):
            trial.set_user_attr("failure_reason", "resource_limit")
            log_hpo_trial_failure(comet_experiment, trial_dir, "resource_limit")
            safe_comet_call(comet_experiment, "end")
            raise optuna.TrialPruned(f"Trial exceeded available memory. See {stderr_path}")
        trial.set_user_attr("failure_reason", "subprocess_error")
        log_hpo_trial_failure(comet_experiment, trial_dir, "subprocess_error")
        safe_comet_call(comet_experiment, "end")
        raise RuntimeError(f"Training subprocess failed with exit code {completed.returncode}. See {stderr_path}")

    result_path = trial_dir / "result.json"
    if not result_path.is_file():
        log_hpo_trial_failure(comet_experiment, trial_dir, "missing_result_json")
        safe_comet_call(comet_experiment, "end")
        raise RuntimeError(f"Training finished but did not write {result_path}.")

    result = json.loads(result_path.read_text(encoding="utf-8"))
    trial.set_user_attr("best_model_path", result.get("best_model_path"))
    trial.set_user_attr("global_step", result.get("global_step"))
    trial.set_user_attr("train_rows", result.get("train_rows"))
    trial.set_user_attr("val_rows", result.get("val_rows"))
    log_hpo_trial_success(comet_experiment, result, trial_dir)
    safe_comet_call(comet_experiment, "end")
    return result


def objective(trial: optuna.Trial) -> float:
    result = run_trial_subprocess(trial)
    metric_name = os.getenv("HPO_OBJECTIVE_METRIC", "best_monitor_score")
    metric_value = result.get(metric_name)
    if metric_value is None:
        raise RuntimeError(f"Training result did not contain {metric_name}.")
    trial.report(float(metric_value), step=int(result.get("global_step") or 0))
    return float(metric_value)


def build_comet_callback(study):
    if not hpo_comet_enabled():
        return None
    if CometCallback is None:
        print(
            "[HPO COMET WARNING] optuna-integration is not installed; "
            "install `optuna-integration>=4.0.0` for native Optuna Comet logging.",
            file=sys.stderr,
        )
        return None
    if not os.getenv("COMET_API_KEY"):
        print("[HPO COMET WARNING] COMET_API_KEY is missing; native Comet logging disabled.", file=sys.stderr)
        return None

    project_name = os.getenv("HPO_COMET_PROJECT_NAME") or os.getenv("COMET_PROJECT_NAME") or "diffcoder-hpo"
    workspace = os.getenv("HPO_COMET_WORKSPACE") or os.getenv("COMET_WORKSPACE")
    metric_name = os.getenv("HPO_OBJECTIVE_METRIC", "best_monitor_score")
    return CometCallback(
        study,
        workspace=workspace,
        project_name=project_name,
        metric_names=[metric_name],
    )


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
    default_direction = "maximize" if os.getenv("CHECKPOINT_MODE", "max") == "max" else "minimize"
    study = optuna.create_study(
        study_name=study_name,
        storage=storage,
        direction=os.getenv("HPO_DIRECTION", default_direction),
        load_if_exists=True,
        sampler=sampler,
        pruner=pruner,
    )

    comet_callback = build_comet_callback(study)
    objective_fn = objective
    callbacks = []
    if comet_callback is not None:
        objective_fn = comet_callback.track_in_comet()(objective_fn)
        callbacks.append(comet_callback)

    study.optimize(
        objective_fn,
        n_trials=env_int("HPO_N_TRIALS", 20),
        timeout=None if env_int("HPO_TIMEOUT_SECONDS", 0) <= 0 else env_int("HPO_TIMEOUT_SECONDS", 0),
        callbacks=callbacks,
        catch=(RuntimeError,),
        gc_after_trial=True,
    )

    complete_trials = [trial for trial in study.trials if trial.state == optuna.trial.TrialState.COMPLETE]
    if not complete_trials:
        print("No completed trials yet. Check hpo_trials/*/stderr.log for failures.")
        return

    print(f"Best value: {study.best_value}")
    print(f"Best params: {study.best_params}")
    print(f"Best trial dir: {study.best_trial.user_attrs.get('trial_dir')}")


if __name__ == "__main__":
    main()
