def parse_ini_config(config_str):
    sections = config_str.strip().split('\n\n')
    result = {}

    for section in sections:
        lines = section.split('\n')
        if lines[0].startswith('[') and lines[0].endswith(']'):
            section_name = lines[0][1:-1]
            result[section_name] = {}
        else:
            continue

        for line in lines[1:]:
            key, value = line.split('=')
            result[section_name][key.strip()] = value.strip()

    return result

if __name__ == '__main__':
    config_str = """
    [database]
    host=localhost
    port=5432

    [logging]
    level=INFO
    file=app.log
    """

    print(parse_ini_config(config_str))