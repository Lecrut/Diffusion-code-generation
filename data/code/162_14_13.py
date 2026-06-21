def map_config_to_defaults(config):
    if not isinstance(config, dict):
        raise ValueError("Input must be a dictionary")
    
    defaults = {
        'debug': False,
        'enabled': True,
        'timeout': 30
    }
    
    return {key: config.get(key, default) for key, default in defaults.items()}

if __name__ == '__main__':
    sample_config = {'debug': True, 'timeout': 60}
    print(map_config_to_defaults(sample_config))