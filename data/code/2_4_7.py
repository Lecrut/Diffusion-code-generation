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
            raise ValueError(f"Invalid numeric value: {stripped}")
    return result

if __name__ == '__main__':
    sample_input = "10.5, 20, 30.0, invalid"
    try:
        output = parse_volumes(sample_input)
        print(output)
    except ValueError as e:
        print(f"Error: {e}")