def map_config_to_defaults(config):
    return {
        'debug': config.get('debug', False),
        'enabled': config.get('enabled', True),
        'timeout': config.get('timeout', 30)
    }

if __name__ == '__main__':
    sample_config = {'debug': True, 'timeout': 60}
    print(map_config_to_defaults(sample_config))