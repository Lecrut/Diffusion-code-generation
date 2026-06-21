def map_config_to_defaults(config):
    return {
        'enable_feature': config.get('enable_feature', False),
        'log_level': config.get('log_level', 'INFO'),
        'timeout': config.get('timeout', 30)
    }

if __name__ == '__main__':
    sample_config = {
        'enable_feature': True,
        'log_level': 'DEBUG'
    }
    print(map_config_to_defaults(sample_config))