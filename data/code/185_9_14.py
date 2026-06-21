def parse_ini_config(config_str):
    config_dict = {}
    current_section = None

    for line in config_str.split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        elif line.startswith('[') and line.endswith(']'):
            current_section = line[1:-1]
            config_dict[current_section] = {}
        else:
            key, value = line.split('=')
            config_dict[current_section][key.strip()] = value.strip()

    return config_dict

if __name__ == '__main__':
    sample_config = """
    [database]
    host=localhost
    port=5432
    user=admin
    password=secret

    [logging]
    level=INFO
    file_path=/var/log/app.log
    """

    parsed_config = parse_ini_config(sample_config)
    print(parsed_config)