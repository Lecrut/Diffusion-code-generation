class ConfigMapper:
    def __init__(self):
        self.config_mapping = {
            ('host', 'localhost'): '127.0.0.1',
            ('port', 8080): 'HTTP_PORT',
            ('debug', True): 'DEBUG_MODE'
        }

    def get_config_value(self, key):
        return self.config_mapping.get(key)

if __name__ == '__main__':
    mapper = ConfigMapper()
    print(mapper.get_config_value(('host', 'localhost')))
    print(mapper.get_config_value(('port', 8080)))
    print(mapper.get_config_value(('debug', True)))