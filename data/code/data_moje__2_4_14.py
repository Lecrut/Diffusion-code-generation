def parse_volumes(volume_string):
    volumes = []
    parts = volume_string.split(',')
    for part in parts:
        part = part.strip()
        if part == '':
            continue
        try:
            value = float(part)
            volumes.append(value)
        except ValueError:
            raise ValueError(f"Invalid numeric value: {part}")
    return volumes

if __name__ == '__main__':
    sample_input = "1.5, 2.7, 3.14, 4.0"
    result = parse_volumes(sample_input)
    print(result)
    error_input = "1.5, abc, 3.14"
    try:
        parse_volumes(error_input)
    except ValueError as e:
        print(e)