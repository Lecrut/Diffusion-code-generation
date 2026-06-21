def map_config_to_defaults(config):
    return {
        'debug': config.get('debug', False),
        'verbose': config.get('verbose', True),
        'enabled': config.get('enabled', True)
    }

if __name__ == '__main__':
    sample_config = {'debug': True, 'enabled': False}
    print(map_config_to_defaults(sample_config))