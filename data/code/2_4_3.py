def parse_volumes(volume_string):
    if not isinstance(volume_string, str):
        raise TypeError("Input must be a string")
    
    if volume_string.strip() == "":
        return []
    
    parts = volume_string.split(",")
    result = []
    
    for part in parts:
        stripped = part.strip()
        if stripped == "":
            continue
        try:
            value = float(stripped)
            result.append(value)
        except ValueError:
            raise ValueError(f"Non-numeric input found: '{stripped}'")
    
    return result

if __name__ == '__main__':
    sample_input = "10.5, 20.0, 30.25, invalid, 40"
    try:
        volumes = parse_volumes(sample_input)
        print(volumes)
    except ValueError as e:
        print(f"Error: {e}")