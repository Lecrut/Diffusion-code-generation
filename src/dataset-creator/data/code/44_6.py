import json
from pathlib import Path
def parse_nested_env(env_vars: dict) -> str:
    def get_value(key_path):
        current = env_vars
        for key in key_path.split('.'):
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return None
        return current
    result_parts = []
    target_path = 'app.name.production.mode'
    value = get_value(target_path)
    if isinstance(value, str):
        return f"Configured for {value}"
    elif isinstance(value, dict):
        json_str = json.dumps(value)
        return f"Configuration loaded: {json_str}"
    else:
        return "Invalid configuration type found."
if __name__ == '__main__':
    sample_env_vars = {
        'app.name.production.mode': 'active',
        'database.host.port.timeout.connection_pool.size': {
            'host': 'localhost',
            'port': 5432,
            'timeout': 10,
            'connection_pool_size': 100
        },
        'logging.level.format.color.enabled': True
    }
    output = parse_nested_env(sample_env_vars)
    print(output)