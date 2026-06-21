def parse_ini(config_str):
    result = {}
    current_section = None

    for line in config_str.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        elif line.startswith('[') and line.endswith(']'):
            current_section = line[1:-1]
            if current_section not in result:
                result[current_section] = {}
        else:
            key, value = line.split('=')
            key = key.strip()
            value = value.strip()
            if current_section:
                result[current_section][key] = value
            else:
                result[key] = value

    return result

if __name__ == '__main__':
    config_str = """
[section1]
key1=value1
key2=value2

[section2]
key3=value3
"""
    print(parse_ini(config_str))