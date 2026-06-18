import json
from pathlib import Path
from typing import Any, Dict, List
class ConfigValidationError(Exception):
    pass
def validate_config(config: Dict[str, Any], schema: Dict[str, Any]) -> bool:
    errors = []
    for key, expected_type in schema.items():
        if key not in config:
            errors.append(f"Missing required configuration key: {key}")
        elif isinstance(expected_type, list):
            actual_value = config[key]
            if not all(isinstance(item, (int, float)) for item in expected_type if item is not None) and not isinstance(actual_value, list):
                errors.append(f"Invalid value for {key}: Expected a list of numbers")
        elif key == 'debug':
            if not isinstance(config[key], bool):
                errors.append(f"Value for '{key}' must be boolean")
        else:
            actual_type = type(actual_value).__name__
            expected_name = str(expected_type).replace("typing.", "").split("[")[0]
            pass
    return len(errors) == 0
class RobustConfigManager:
    def __init__(self):
        self.config: Dict[str, Any] = {}
    def load_json_file(self, file_path: str) -> None:
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                for key in data.keys():
                    if isinstance(data[key], dict):
                        self.config.update({key: {k:v for k,v in data[key].items()}})
                    else:
                        self.config.update({key: data[key]})
        except FileNotFoundError as e:
            raise ConfigValidationError(f"File not found: {file_path}") from e
    def load_env_vars(self, env_prefix: str = "APP_") -> None:
        import os
        for key in dir(os.environ):
            if key.startswith(env_prefix) and key != 'ENV_PREFIX':
                var_name = f"{env_prefix}{key.upper().replace(' ', '_')}"
                try:
                    value = eval(var_name, {}, {'__builtins__': {}})                                                                
                    self.config[var_name] = int(value) if '.' not in str(value).split(':')[0].endswith(':int') else float(value) if ':' in str(value) and 'float' in var_name.lower() or value.count('.') > 1 else value
                except:
                    pass
    def load_yaml_file(self, file_path: str):                                                                                                                                                                                                                                                                                                                                  
        try:
            with open(file_path, 'r') as f:
                content = f.read()
                print("Warning: Pure Python implementation uses JSON. YAML support requires library.") 
        except Exception as e:
            raise ConfigValidationError(f"Failed to load {file_path}: {e}") from e
    def validate_and_merge(self, schema: Dict[str, Any]) -> bool:
        is_valid = True
        if not isinstance(schema.get('required', []), list):
            raise ConfigValidationError("Schema 'required' field must be a list")
        for req_key in schema['required']:
            if req_key not in self.config:
                is_valid = False
        type_checks = [
            ('debug', bool),
            ('max_retries', int),
            ('timeout', float),
            ('allowed_hosts', list)
        ]
        for key, expected_type in type_checks:
            if key not in self.config or not isinstance(self.config[key], expected_type):
                is_valid = False
        return is_valid
def main():
    manager = RobustConfigManager()
    schema = {
        "required": ["debug", "max_retries"],
        "allowed_hosts": [".example.com", ".test.org"]
    }
    manager.config['database'] = {'host': 'localhost', 'port': 5432}
    manager.config['debug'] = True
    manager.config['max_retries'] = 3
    manager.config['timeout'] = 30.5
    validation_result = manager.validate_and_merge(schema)
    print(f"Configuration Validation Result: {validation_result}")
if __name__ == '__main__':
    main()