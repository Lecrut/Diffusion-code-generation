def map_config_to_defaults(config):
    defaults = {
        'enable_feature': False,
        'log_debug': True,
        'max_connections': 100,
        'use_ssl': False
    }
    return {key: config.get(key, default) for key, default in defaults.items()}

if __name__ == '__main__':
    sample_config = {
        'enable_feature': True,
        'log_debug': False
    }
    print(map_config_to_defaults(sample_config))