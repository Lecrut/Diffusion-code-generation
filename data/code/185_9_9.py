import re

def parse_ini_config(config_string):
    config_dict = {}
    current_section = None
    for line in config_string.split('\n'):
        if line.strip() and not line.startswith('#'):
            if line.startswith('[') and line.endswith(']'):
                current_section = line[1:-1].strip()
                config_dict[current_section] = {}
            else:
                key, value = line.split('=')
                if current_section:
                    config_dict[current_section][key.strip()] = value.strip()
    return config_dict

if __name__ == '__main__':
    sample_config = """
    [database]
    host=localhost
    port=5432

    [logging]
    level=DEBUG
    file=app.log
    """

    parsed_config = parse_ini_config(sample_config)
    print(parsed_config)