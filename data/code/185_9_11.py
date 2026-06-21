def parse_ini_config(config_str):
    config = {}
    current_section = None
    for line in config_str.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        elif line.startswith('[') and line.endswith(']'):
            current_section = line[1:-1]
            config[current_section] = {}
        else:
            key, value = line.split('=')
            key = key.strip()
            value = value.strip()
            if current_section:
                config[current_section][key] = value
            else:
                config[key] = value
    return config

class IniConfigParser:

    def __init__(self, config_str):
        self.config = parse_ini_config(config_str)

    def get_value(self, section, key):
        return self.config.get(section, {}).get(key, None)
if __name__ == '__main__':
    ini_config_str = '\n[section1]\nkey1=value1\nkey2=value2\n\n[section2]\nkey3=value3\n'
    parser = IniConfigParser(ini_config_str)
    print(parser.get_value('section1', 'key1'))
    print(parser.get_value('section2', 'key3'))
    print(parser.get_value('section1', 'nonexistent_key'))