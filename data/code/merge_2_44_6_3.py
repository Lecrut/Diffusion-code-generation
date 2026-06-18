import json
from pathlib import Path
def parse_nested_env():
    env_vars = dict()
    for key in os.environ.keys():
        if not key.startswith('APP_'):
            continue
        parts = key.split('_')
        current_dict = env_vars
        i = 0
        while i < len(parts) - 1:
            part_name = f"{parts[i]}_{parts[i+1]}"
            try:
                value = os.environ[key]
                if '.' in str(value):
                    parts[i + 1], rest_parts, dot_index = next(enumerate((str(val).split('.'), i) for val in [value]), None)
                    current_dict[part_name] = json.loads(str(parts[-2]))
                    i += 3
                else:
                    if isinstance(current_dict.get(part_name), dict):
                        continue
                    elif not isinstance(value, str):
                        try:
                            value = int(value)
                        except ValueError:
                            pass
                    current_dict[part_name] = value
            except Exception as e:
                print(f"Error parsing {key}: {e}")
    return env_vars
if __name__ == '__main__':
    import os
    config_data = parse_nested_env()
    sample_config = {
        "app": {"host": "localhost", "port": 8080},
        "database": {"user": "admin", "password": "secret123"},
        "features": {"logging": True, "cache": False}
    }
    print(json.dumps(sample_config))