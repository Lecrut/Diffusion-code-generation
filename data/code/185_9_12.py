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
            if current_section:
                config_dict[current_section][key] = value
            else:
                config_dict[key] = value

    return config_dict

if __name__ == '__main__':
    sample_config = """
[section1]
key1=value1
key2=value2

[section2]
key3=value3
"""
    print(parse_ini(sample_config))