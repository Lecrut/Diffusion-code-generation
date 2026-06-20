def parse_volumes(volume_string):
    if not isinstance(volume_string, str):
        raise TypeError("Input must be a string")
    
    parts = volume_string.split(',')
    result = []
    
    for part in parts:
        stripped_part = part.strip()
        if not stripped_part:
            continue
        
        try:
            value = float(stripped_part)
            result.append(value)
        except ValueError:
            raise ValueError(f"Non-numeric value found: {stripped_part}")
    
    return result

if __name__ == '__main__':
    sample_input = "10.5, 20, 30.0, invalid, 40.25"
    try:
        output = parse_volumes(sample_input)
        print(output)
    except ValueError as e:
        print(f"Error: {e}")