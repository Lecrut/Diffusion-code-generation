class ConfigMapper:
    DEFAULTS = {
        'debug': False,
        'enabled': True,
        'timeout': 30
    }
    
    @staticmethod
    def map_config_to_defaults(config):
        return {key: config.get(key, default) for key, default in ConfigMapper.DEFAULTS.items()}

if __name__ == '__main__':
    mapper = ConfigMapper()
    sample_config = {'debug': True, 'timeout': 60}
    print(mapper.map_config_to_defaults(sample_config))