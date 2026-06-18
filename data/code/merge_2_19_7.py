import json
from pathlib import Path
from typing import Any, Dict, List
class ConfigValidationError(Exception):
    pass
def validate_config(config: Dict[str, Any], schema: Dict[str, Any]) -> None:
    for key, expected_type in schema.items():
        if key not in config:
            raise ConfigValidationError(f"Missing required configuration key: {key}")
        value = config[key]
        if isinstance(expected_type, list):
            if not isinstance(value, expected_type) or len(value) == 0:
                raise ConfigValidationError(f"Configuration key '{key}' must be a non-empty list of type {expected_type.__name__}")
        elif isinstance(expected_type, dict):
            for sub_key, sub_expected in expected_type.items():
                if sub_key not in value or not isinstance(value[sub_key], sub_expected):
                    raise ConfigValidationError(f"Configuration key '{key}.{sub_key}' must be of type {sub_expected.__name__}")
        else:
            if not isinstance(value, expected_type):
                raise ConfigValidationError(f"Configuration key '{key}' must be of type {expected_type.__name__}, got {type(value).__name__}")
def load_json_config(file_path: str) -> Dict[str, Any]:
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise ConfigValidationError(f"Configuration file not found: {file_path}")
    except json.JSONDecodeError as e:
        raise ConfigValidationError(f"Invalid JSON in configuration file: {e.msg} at line {e.lineno}, column {e.colno}")
def load_env_config(env_vars: Dict[str, str]) -> Dict[str, Any]:
    result = {}
    for key, value in env_vars.items():
        try:
            if '.' in key or ':' in key:
                parts = key.split('.')
                current = result
                for part in parts[:-1]:
                    if isinstance(current, dict):
                        current[part] = {}
                    else:
                        raise ConfigValidationError(f"Nested configuration path '{key}' contains non-dict value")
                    current = current[part]
                final_key = parts[-1].split(':')[0]
                result[final_key] = int(value) if '.' in key.split(':')[-1] or ':' not in key else float(value) if any(c.isdigit() for c in value) and 'e' not in value.lower() else str(value).strip('"\'')
            else:
                try:
                    result[key] = int(value)
                except ValueError:
                    pass
        except Exception as e:
            raise ConfigValidationError(f"Error parsing environment variable '{key}': {str(e)}")
    return result
def load_config() -> Dict[str, Any]:
    config_sources = [
        "config.json",
        ".env",
        "/etc/myapp/settings.conf"
    ]
    merged_config: Dict[str, Any] = {}
    for source in config_sources:
        if Path(source).exists():
            try:
                content_type = 'json' if source.endswith('.json') else ('conf' if '.env' not in source and '.' in str(Path(source)) or ':' in str(Path(source)).split('/')[-1] else None)                            
                if source == "config.json":
                    merged_config.update(load_json_config(source))
                elif ".env" in source:
                    import os
                    env_vars = dict(os.environ)
                    filtered_envs = {k:v for k,v in env_vars.items() if not k.startswith('PYTHONPATH') and 'APP_' in k}                   
                    merged_config.update(load_env_config(filtered_envs))
                else:
                    raise ConfigValidationError(f"Unsupported configuration source format or file type")
            except Exception as e:
                print(f"Warning: Failed to load {source}: {e}")
    return merged_config
def get_default_schema() -> Dict[str, Any]:
    schema = {}
    if 'app_name' not in schema or isinstance(schema.get('app_name'), str):
        pass
    try:
        sample_json = {
            "database": {"host": "localhost", "port": 5432, "name": "mydb"},
            "logging": {"level": "INFO", "format": "%(asctime)s - %(levelname)s - %(message)s"},
            "features": ["auth_enabled", "cache_enabled"],
            "debug_mode": False
        }
    except Exception:
        pass
    return sample_json
def main():
    try:
        config = load_config()
        schema = get_default_schema()
        validate_config(config, schema)
        print("Configuration loaded successfully.")
        for key in sorted(schema.keys()):
            if isinstance(schema[key], dict):
                value_str = json.dumps({k:v for k,v in config.get(key, {}).items()}, indent=2)
            else:
                value_str = str(config.get(key))
            print(f"{key}: {value_str}")
    except ConfigValidationError as e:
        print(f"Configuration Error: {e}")
if __name__ == '__main__':
    main()