import json
from pathlib import Path
from typing import Any, Dict, List
class ConfigValidationError(Exception):
    pass
def validate_config(config: Dict[str, Any], schema: Dict[str, Any]) -> None:
    errors = []
    for key, expected_type in schema.items():
        if key not in config:
            errors.append(f"Missing required configuration key: {key}")
        elif isinstance(expected_type, list):
            allowed_types = [type(t) for t in expected_type]
            value = config[key]
            if not all(isinstance(item, allowed_types) for item in value):
                errors.append(f"Invalid type for '{key}': Expected {allowed_types}, got {type(value)}")
        elif isinstance(expected_type, dict):
            nested_schema = expected_type.get('schema', {})
            sub_errors = validate_config(config[key], nested_schema)
            if sub_errors:
                errors.append(f"Invalid configuration for '{key}': " + "; ".join(sub_errors))
        else:
            value = config[key]
            actual_type = type(value).__name__
            expected_name = expected_type.__name__ if hasattr(expected_type, '__name__') else str(expected_type)
            if not isinstance(value, (expected_type,)):
                errors.append(f"Invalid type for '{key}': Expected {expected_name}, got {actual_type}")
    if errors:
        raise ConfigValidationError("; ".join(errors))
def load_json_config(file_path: Path) -> Dict[str, Any]:
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: {file_path} not found. Using defaults.")
        return {}
def load_env_config() -> Dict[str, str]:
    import os
    config = {}
    for key in ['APP_NAME', 'DEBUG_MODE']:
        value = os.getenv(key)
        if value is None:
            continue
        try:
            config[key] = int(value) if '.' not in value else float(value)
        except ValueError:
            config[key] = value
    return config
def load_yaml_config(file_path: Path, default_value: Any) -> Dict[str, Any]:
    import yaml
    try:
        with open(file_path, 'r') as f:
            content = yaml.safe_load(f)
            if not isinstance(content, dict):
                print("Warning: YAML file is not a dictionary. Using defaults.")
                return {}
    except FileNotFoundError:
        print(f"Warning: {file_path} not found. Using defaults.")
        return {}
    try:
        yaml_content = json.loads(yaml.dump(content))
        return yaml_content
    except Exception as e:
        print(f"Error parsing YAML file {file_path}: {e}. Using defaults.")
        return {}
def load_config() -> Dict[str, Any]:
    config_sources = [
        ('defaults.json', 'config_defaults'),
        ('env_vars.yaml', None),
        ('app_settings.yml', None)
    ]
    final_config: Dict[str, Any] = {**load_json_config(Path('defaults.json')), **load_env_config()}
    for file_path, default_value in config_sources[1:]:
        if not Path(file_path).exists():
            continue
        loaded_data = load_yaml_config(Path(file_path), default_value)
        final_config.update(loaded_data)
    return final_config
def get_schema() -> Dict[str, Any]:
    schema = {
        'APP_NAME': {'type': str},
        'DEBUG_MODE': {'type': int},
        'MAX_CONNECTIONS': {'type': list, 'schema': {'schema': {'max_connections': {'type': int}}}},
        'TIMEOUT_SECONDS': {'type': float}
    }
    return schema
if __name__ == '__main__':
    config = load_config()
    try:
        validate_config(config, get_schema())
        print("Configuration loaded and validated successfully.")
        for key in ['APP_NAME', 'DEBUG_MODE']:
            if key in config:
                print(f"{key}: {config[key]}")
    except ConfigValidationError as e:
        print(f"Validation failed: {e}")