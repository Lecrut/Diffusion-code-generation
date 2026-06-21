class ConfigMapping:
    def __init__(self):
        self.mapping = {
            ('host', 'localhost'): '127.0.0.1',
            ('port', 8080): 'HTTP_PORT',
            ('debug', True): 'DEBUG_MODE'
        }

    def get_value(self, key):
        if not isinstance(key, tuple) or len(key) != 2:
            raise ValueError("Key must be a two-element tuple")
        return self.mapping.get(key, None)

if __name__ == '__main__':
    config = ConfigMapping()
    print(config.get_value(('host', 'localhost')))
    print(config.get_value(('port', 8080)))
    print(config.get_value(('debug', True)))