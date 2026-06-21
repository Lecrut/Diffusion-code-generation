def parse_ini(config_string):
    config_dict = {}
    current_section = None

    for line in config_string.splitlines():
        if line.strip() and not line.startswith('#'):
            if line.startswith('[') and line.endswith(']'):
                current_section = line[1:-1].strip()
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

    parsed_config = parse_ini(sample_config)
    print(parsed_config)