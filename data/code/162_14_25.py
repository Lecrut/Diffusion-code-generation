def validate_config(config):
    expected_keys = {'debug', 'enabled', 'timeout'}
    if not isinstance(config, dict) or not expected_keys.issubset(config):
        raise ValueError("Invalid configuration: missing required keys")

def map_config_to_defaults(config):
    validate_config(config)
    return {
        'debug': config.get('debug', False),
        'enabled': config.get('enabled', True),
        'timeout': config.get('timeout', 30)
    }

if __name__ == '__main__':
    sample_config = {'debug': True, 'timeout': 60}
    print(map_config_to_defaults(sample_config))