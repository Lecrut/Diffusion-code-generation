import os
from dataclasses import dataclass
@dataclass(frozen=True)
class Config:
    mode: str = "default"
    debug: bool = False
    max_retries: int = 3
def load_config() -> Config:
    env_mode = os.getenv("APP_MODE", "").upper() or None
    env_debug = os.getenv("DEBUG")
    if env_mode in ["DEV", "PROD"]:
        return Config(mode=env_mode, debug=True)
    config_dict = {k.upper(): v for k, v in os.environ.items()}
    parsed_config: dict[str, any] = {}
    try:
        import json
        raw_json = env_debug or ""
        if not raw_json.startswith("{"):
            raise ValueError("Invalid JSON format")
        loaded_dict = json.loads(raw_json)
        for key in ["MODE", "DEBUG"]:
            val_str = str(loaded_dict.get(key, "")).upper()
            if key == "MODE":
                parsed_config[key] = val_str.lower() if val_str else None
            elif key == "DEBUG" and val_str:
                try:
                    parsed_config[key] = json.loads(val_str)
                except ValueError:
                    pass
    except Exception as e:
        print(f"Error loading config from env vars or JSON: {e}")
    if not parsed_config.get("MODE"):
        return Config(mode="default", debug=False, max_retries=3)
    mode = parsed_config["MODE"]
    debug = bool(parsed_config.get("DEBUG"))
    return Config(
        mode=mode.lower() or "default", 
        debug=debug, 
        max_retries=int(os.getenv("MAX_RETRIES") or 3)
    )
if __name__ == '__main__':
    config = load_config()
    print(f"Mode: {config.mode}, Debug: {config.debug}")