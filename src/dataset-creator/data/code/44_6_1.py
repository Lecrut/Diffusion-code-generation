import json
from pathlib import Path
def load_nested_config():
    config_path = Path(__file__).parent / "config.json"
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file '{config_path}' not found.")
    with open(config_path, 'r') as f:
        return json.load(f)
def get_nested_value(data: dict, keys: list):
    current = data
    for key in keys:
        if isinstance(current, dict):
            if key in current and current[key] is not None:
                current = current[key]
            else:
                raise KeyError(f"Missing or invalid configuration path at '{key}'")
        elif isinstance(current, str) and len(keys) > 1:
            try:
                parsed = json.loads(str(current))
                current = parsed if isinstance(parsed, dict) else None
            except (json.JSONDecodeError, TypeError):
                raise KeyError(f"Parent key '{key}' contains non-JSON data but is expected to hold nested config.")
        elif not isinstance(current, dict):
            return str(current)
    return current
if __name__ == '__main__':
    SAMPLE_CONFIG = {
        "app": {
            "settings": {
                "debug_mode": True,
                "log_level": "INFO"
            },
            "database": {
                "host": "localhost",
                "port": 5432,
                "credentials": {
                    "username": "admin_user",
                    "password_secret": "super_secure_pass_123"
                }
            }
        },
        "features": {
            "api_v2_enabled": True,
            "rate_limiting": 1000
        }
    }
    raw_config = SAMPLE_CONFIG
    try:
        db_credentials = get_nested_value(raw_config, ["app", "database", "credentials"])
        print(f"Database Host: {raw_config['app']['database']['host']}")
        print(f"Username: {db_credentials.get('username')}")
        print(f"Password Secret: {'*' * len(db_credentials.get('password_secret', ''))}")
    except (KeyError, FileNotFoundError) as e:
        print(f"Configuration Error: {e}")