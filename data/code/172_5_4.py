config_mapping = {
    ('host', 'localhost'): '127.0.0.1',
    ('port', 8080): 'HTTP_PORT',
    ('debug', True): 'DEBUG_MODE'
}

if __name__ == '__main__':
    print(config_mapping[('host', 'localhost')])
    print(config_mapping.get(('port', 8080), 'DEFAULT_PORT'))
    print(config_mapping.get(('debug', False), 'NOT_DEBUG'))