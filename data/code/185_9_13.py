import re

def parse_ini_config(config_str):
    config_dict = {}
    current_section = None
    lines = config_str.strip().split('\n')
    
    for line in lines:
        if line.startswith('[') and line.endswith(']'):
            current_section = line[1:-1].strip()
            if current_section not in config_dict:
                config_dict[current_section] = {}
        elif '=' in line and current_section is not None:
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip()
            if key not in config_dict[current_section]:
                config_dict[current_section][key] = value
    
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
    file=app.log
    """
    
    parsed_config = parse_ini_config(sample_config)
    print(parsed_config)