def parse_volumes(volume_string):
    if not isinstance(volume_string, str):
        raise TypeError("Input must be a string")
    
    if not volume_string.strip():
        return []
    
    parts = volume_string.split(',')
    result = []
    for part in parts:
        stripped = part.strip()
        if not stripped:
            continue
        try:
            value = float(stripped)
            result.append(value)
        except ValueError:
            raise ValueError(f"Non-numeric input detected: '{stripped}'")
    return result

if __name__ == '__main__':
    sample_input = "1.5, 2.0, -3.14, 0, abc"
    try:
        result = parse_volumes(sample_input)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")