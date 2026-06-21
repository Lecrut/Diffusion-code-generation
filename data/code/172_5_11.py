class ConfigMapper:
    def __init__(self):
        self.config_mapping = {
            ('host', 'localhost'): '127.0.0.1',
            ('port', 8080): 'HTTP_PORT',
            ('debug', True): 'DEBUG_MODE'
        }

    def get_config(self, key):
        return self.config_mapping.get(key, None)

if __name__ == '__main__':
    config_mapper = ConfigMapper()
    print(config_mapper.get_config(('host', 'localhost')))
    print(config_mapper.get_config(('port', 8080)))
    print(config_mapper.get_config(('debug', True)))