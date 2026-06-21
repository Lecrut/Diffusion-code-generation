def parse_ini(config_str):
    config_dict = {}
    current_section = None

    for line in config_str.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        elif line.startswith('[') and line.endswith(']'):
            current_section = line[1:-1]
            config_dict[current_section] = {}
        else:
            key, value = line.split('=')
            key = key.strip()
            value = value.strip()
            if current_section in config_dict:
                config_dict[current_section][key] = value
            else:
                config_dict['DEFAULT'] = {key: value}

    return config_dict

if __name__ == '__main__':
    ini_config = """
    [database]
    host=localhost
    port=5432
    user=admin
    password=secret

    [logging]
    level=INFO
    file=app.log
    """
    parsed_config = parse_ini(ini_config)
    print(parsed_config)