def parse_volumes(input_string):
    parts = input_string.split(',')
    result = []
    for part in parts:
        stripped = part.strip()
        if not stripped:
            continue
        try:
            value = float(stripped)
            result.append(value)
        except ValueError:
            raise ValueError(f"Invalid volume value: {stripped}")
    return result

if __name__ == '__main__':
    sample_data = "10.5, 20, 30.25, invalid, 40"
    try:
        volumes = parse_volumes(sample_data)
        print(volumes)
    except ValueError as e:
        print(f"Error: {e}")
    sample_valid = "5.0, 10, 15.5, 20"
    valid_volumes = parse_volumes(sample_valid)
    print(valid_volumes)