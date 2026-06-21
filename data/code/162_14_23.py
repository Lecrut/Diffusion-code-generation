def map_config_to_defaults(config):
    defaults = {
        'log_enabled': True,
        'max_workers': 5,
        'retry_attempts': 3,
        'ssl_required': False
    }
    return {key: config.get(key, default) for key, default in defaults.items()}

if __name__ == '__main__':
    sample_config = {'log_enabled': False, 'retry_attempts': 5}
    print(map_config_to_defaults(sample_config))