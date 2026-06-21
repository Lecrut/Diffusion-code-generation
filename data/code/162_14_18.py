def map_config_to_defaults(config):
    defaults = {
        'enable_logging': True,
        'retry_attempts': 3,
        'cache_enabled': False,
        'max_retries': 5
    }
    return {key: config.get(key, default) for key, default in defaults.items()}

if __name__ == '__main__':
    sample_config = {
        'enable_logging': False,
        'retry_attempts': 2
    }
    print(map_config_to_defaults(sample_config))