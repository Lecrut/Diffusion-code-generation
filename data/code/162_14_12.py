def map_config_to_defaults(config):
    defaults = {
        'debug': False,
        'enabled': True,
        'timeout': 30,
        'retry_count': 3,
        'verbose': False
    }
    return {key: config.get(key, default) for key, default in defaults.items()}

if __name__ == '__main__':
    sample_config = {'debug': True, 'timeout': 60}
    print(map_config_to_defaults(sample_config))