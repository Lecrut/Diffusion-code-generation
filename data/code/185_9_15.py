def parse_ini_config(config_str):
    config_dict = {}
    lines = config_str.strip().split('\n')
    current_section = None

    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        elif line.startswith('[') and line.endswith(']'):
            current_section = line[1:-1]
            if current_section not in config_dict:
                config_dict[current_section] = {}
        else:
            key, value = line.split('=')
            key = key.strip()
            value = value.strip().strip('"')
            if current_section:
                config_dict[current_section][key] = value
            else:
                config_dict[key] = value

    return config_dict

if __name__ == '__main__':
    ini_config = """[Section1]
key1=value1
key2="value 2"

[section2]
key3=value3"""

    print(parse_ini_config(ini_config))