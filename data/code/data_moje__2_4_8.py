def parse_volumes(volume_string):
    parts = volume_string.split(',')
    result = []
    for part in parts:
        stripped = part.strip()
        if stripped == '':
            continue
        try:
            value = float(stripped)
            result.append(value)
        except ValueError:
            raise ValueError(f"Non-numeric value encountered: {stripped}")
    return result

if __name__ == '__main__':
    sample_input = "1.5, 2.7, 3.14, 42.0"
    parsed = parse_volumes(sample_input)
    print(parsed)
    
    invalid_input = "1.5, abc, 3.14"
    try:
        parse_volumes(invalid_input)
    except ValueError as e:
        print(e)
    
    empty_input = ""
    print(parse_volumes(empty_input))