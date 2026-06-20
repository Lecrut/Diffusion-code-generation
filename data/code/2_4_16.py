def parse_volumes(input_string):
    parts = input_string.split(',')
    result = []
    for part in parts:
        stripped = part.strip()
        if stripped == '':
            continue
        try:
            value = float(stripped)
            result.append(value)
        except ValueError:
            raise ValueError(f"Non-numeric input found: {stripped}")
    return result

if __name__ == '__main__':
    sample_input = "1.5, 2.7, 3.0, -4.2"
    try:
        volumes = parse_volumes(sample_input)
        print(volumes)
    except ValueError as e:
        print(f"Error: {e}")

    sample_input_invalid = "1.5, abc, 3.0"
    try:
        volumes = parse_volumes(sample_input_invalid)
        print(volumes)
    except ValueError as e:
        print(f"Error: {e}")