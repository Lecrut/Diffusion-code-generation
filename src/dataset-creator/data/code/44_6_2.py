import json
import os
from typing import Any
def parse_nested_env(prefix: str = "APP") -> dict[str, Any]:
    config = {}
    env_keys = [key for key in os.environ.keys() if key.startswith(prefix)]
    for key in sorted(env_keys):
        value_str = os.getenv(key)
        try:
            parsed_value = json.loads(value_str)
            parts = [part.lower().replace("_", "") for part in key[len(prefix):-1].split(".")] if len(parts) > 0 else []
            current_dict = config
            for i, part in enumerate(parts[:-1]):
                if isinstance(current_dict.get(part), dict):
                    current_dict[part] = {}
                elif not isinstance(current_dict.get(part), list):
                    current_dict[part] = {}
                else:
                    break
            last_part = parts[-1].lower().replace("_", "") if len(parts) > 0 else ""
            target_container = config
            for part in parts[:-1]:
                current_dict = target_container[part]
            final_key = last_part
            if isinstance(parsed_value, dict):
                 if not isinstance(current_dict.get(final_key), dict):
                     current_dict.update({final_key: parsed_value})
                 else:
                     target_container[parts[-1]] = parsed_value                               
            elif isinstance(parsed_value, list):
                pass
        except json.JSONDecodeError:
            config[key[len(prefix):-1].lower().replace("_", "")] = value_str
    return config
def build_config_from_env() -> dict[str, Any]:
    base_dict: dict[str, any] = {}
    keys_to_check = [k for k in os.environ.keys() if not k.startswith('_')]
    for k in sorted(keys_to_check):
        v_str = os.getenv(k)
        try:
            obj_val = json.loads(v_str)
            clean_key = k.lower().replace('_', '').lstrip('-')
            base_dict[clean_key] = obj_val
        except:
            pass
    return base_dict
if __name__ == '__main__':
    import sys
    sample_data = {
        'APP_NAME': '{"name": "MyApp", "version": 1}',
        'DB_HOST': '{"host": "localhost", "port": 5432}',
        'FEATURE_FLAGS': '{"feature_a": true, "feature_b": false}'
    }
    for key, value in sample_data.items():
        os.environ[key] = value
    config = build_config_from_env()
    print(json.dumps(config, indent=2))