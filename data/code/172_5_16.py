config_mapping = {
    ('host', 'localhost'): '127.0.0.1',
    ('port', 8080): 'HTTP_PORT',
    ('debug', True): 'DEBUG_MODE'
}

def validate_key(key):
    if not isinstance(key, tuple) or len(key) != 2:
        raise ValueError("Key must be a tuple of two elements")
    return key

def get_config_value(key):
    try:
        validated_key = validate_key(key)
        return config_mapping[validated_key]
    except KeyError:
        return None
    except ValueError as e:
        print(e)
        return None

if __name__ == '__main__':
    print(get_config_value(('host', 'localhost')))
    print(get_config_value(('port', 8080)))
    print(get_config_value(('debug', True)))
    print(get_config_value(('unknown', 'key')))