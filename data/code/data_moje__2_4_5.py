def parse_volumes(volume_string):
    if not isinstance(volume_string, str):
        raise TypeError("Input must be a string")
    
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
            raise ValueError(f"Invalid volume value: '{stripped}'")
            
    return result

if __name__ == '__main__':
    sample_data = "10.5, 20.0, abc, 30.75"
    try:
        parsed = parse_volumes(sample_data)
        print(parsed)
    except ValueError as e:
        print(f"Error: {e}")