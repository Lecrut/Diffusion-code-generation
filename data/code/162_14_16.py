def map_config_to_defaults(config):
    return {
        'enable_feature': config.get('enable_feature', False),
        'log_debug': config.get('log_debug', True),
        'timeout_seconds': config.get('timeout_seconds', 30)
    }

if __name__ == '__main__':
    sample_config = {
        'enable_feature': True,
        'log_debug': False
    }
    print(map_config_to_defaults(sample_config))