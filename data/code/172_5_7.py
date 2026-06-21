class ConfigMapper:
    def __init__(self):
        self.mapping = {
            ('host', 'localhost'): '127.0.0.1',
            ('port', 8080): 'HTTP_PORT',
            ('debug', True): 'DEBUG_MODE'
        }

    def get_value(self, key):
        return self.mapping.get(key, None)

if __name__ == '__main__':
    config = ConfigMapper()
    print(config.get_value(('host', 'localhost')))
    print(config.get_value(('port', 8080)))
    print(config.get_value(('debug', True)))
    print(config.get_value(('unknown_key', 'unknown_value')))