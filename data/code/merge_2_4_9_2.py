import os
from dataclasses import dataclass
@dataclass(frozen=True)
class Config:
    mode: str = "default"
    debug: bool = False
    log_level: str = "INFO"
def load_config() -> Config:
    env_mode = os.getenv("APP_MODE", "").upper()
    if not env_mode or env_mode in ("DEBUG", "PRODUCTION"):
        mode_map = {"DEBUG": "debug", "PRODUCTION": "production"}
        return Config(mode=mode_map.get(env_mode, "default"), debug=True)
    config_file_path = os.getenv("CONFIG_FILE")
    if not config_file_path:
        default_config = {
            "mode": "default",
            "debug": False,
            "log_level": "INFO"
        }
        return Config(**default_config)
    try:
        import json
        with open(config_file_path, 'r') as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("Config file must be a valid JSON object")
        parsed_mode = str(data.get("mode", "default")).lower()
        debug_val = bool(data.get("debug", False))
        log_level_str = data.get("log_level", "INFO").upper()
        return Config(mode=parsed_mode, debug=debug_val, log_level=log_level_str)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Warning: Could not load config from {config_file_path}, using defaults.")
        default_config = {"mode": "default", "debug": False, "log_level": "INFO"}
        return Config(**default_config)
def apply_mode(config: Config):
    if config.mode == "production":
        print(f"Running in PRODUCTION mode. Log level set to {config.log_level}")
    elif config.mode == "debug":
        print("DEBUG MODE ENABLED")
        for i in range(3):
            val = 10 * i + (5 if config.debug else 0)
            print(f"Debug value: {val}", flush=True)
    else:
        print(f"Running in DEFAULT mode. Log level set to {config.log_level}")
if __name__ == '__main__':
    current_config = load_config()
    apply_mode(current_config)