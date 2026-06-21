CONFIG_MAP = {
    ('host', 'localhost'): '127.0.0.1',
    ('port', 8080): 'HTTP_PORT',
    ('debug', True): 'DEBUG_MODE'
}

if __name__ == '__main__':
    print(CONFIG_MAP[('host', 'localhost')])
    print(CONFIG_MAP[('port', 8080)])
    print(CONFIG_MAP[('debug', True)])