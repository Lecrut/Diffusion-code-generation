def parse_volumes(input_string):
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    if not input_string.strip():
        return []
    parts = input_string.split(',')
    result = []
    for part in parts:
        cleaned = part.strip()
        if not cleaned:
            continue
        try:
            value = float(cleaned)
            result.append(value)
        except ValueError:
            raise ValueError(f"Cannot convert '{cleaned}' to a floating-point number")
    return result

if __name__ == '__main__':
    sample_input = "10.5, 20, 30.75, 40"
    volumes = parse_volumes(sample_input)
    print(volumes)
    sample_input_with_error = "10.5, invalid, 30"
    try:
        volumes = parse_volumes(sample_input_with_error)
    except ValueError as e:
        print(e)