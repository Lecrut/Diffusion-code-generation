def map_config_to_defaults(config):
    defaults = {
        'enable_feature': True,
        'log_level': False,
        'debug_mode': True
    }
    return {key: config.get(key, default) for key, default in defaults.items()}

if __name__ == '__main__':
    sample_config = {'log_level': True}
    print(map_config_to_defaults(sample_config))