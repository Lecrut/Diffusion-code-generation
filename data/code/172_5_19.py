CONFIG_MAP = {
    ('host', 'localhost'): '127.0.0.1',
    ('port', 8080): 'HTTP_PORT',
    ('debug', True): 'DEBUG_MODE'
}

def validate_key(key):
    if not isinstance(key, tuple) or len(key) != 2:
        raise ValueError("Key must be a tuple of two elements")
    return key

def get_config_value(config_key):
    key = validate_key(config_key)
    return CONFIG_MAP.get(key, None)

if __name__ == '__main__':
    print(get_config_value(('host', 'localhost')))
    print(get_config_value(('port', 8080)))
    print(get_config_value(('debug', True)))
    print(get_config_value(('unknown', False)))