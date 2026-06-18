def validate_and_retrieve(config: dict, allowed_keys: set) -> list:
    return [config[key] for key in config if key in allowed_keys]
if __name__ == '__main__':
    configuration = {
        'database_host': 'localhost',
        'api_key': 'secret123',
        'timeout': 30,
        'debug_mode': False
    }
    expected_settings = {'database_host', 'api_key'}
    result_values = validate_and_retrieve(configuration, expected_settings)
    print(result_values[0])