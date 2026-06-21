class ConfigMapper:
    DEFAULTS = {
        'debug': False,
        'enabled': True,
        'timeout': 30
    }

    def map_config_to_defaults(self, config):
        return {key: config.get(key, default) for key, default in self.DEFAULTS.items()}

if __name__ == '__main__':
    mapper = ConfigMapper()
    sample_config = {'debug': True, 'timeout': 60}
    mapped_values = mapper.map_config_to_defaults(sample_config)
    print(f"Debug: {mapped_values['debug']}")
    print(f"Enabled: {mapped_values['enabled']}")
    print(f"Timeout: {mapped_values['timeout']}")