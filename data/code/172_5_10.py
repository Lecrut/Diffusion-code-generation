config_mapping = {('host', 'localhost'): '127.0.0.1', ('port', 8080): 'HTTP_PORT', ('debug', True): 'DEBUG_MODE'}

def get_config_value(key):
    if key in config_mapping:
        return config_mapping[key]
    else:
        raise KeyError(f'Key {key} not found in configuration mapping.')
if __name__ == '__main__':
    try:
        print(get_config_value(('host', 'localhost')))
        print(get_config_value(('port', 8080)))
        print(get_config_value(('debug', True)))
        print(get_config_value(('unknown', 'value')))
    except KeyError as e:
        print(e)