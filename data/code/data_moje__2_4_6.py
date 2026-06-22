def parse_volumes(volume_string):
    if not volume_string:
        return []
    parts = volume_string.split(',')
    result = []
    for part in parts:
        value = part.strip()
        try:
            result.append(float(value))
        except ValueError:
            raise ValueError(f"Invalid numeric value: {value}")
    return result

if __name__ == '__main__':
    sample_input = "10.5, 20, 30.25, invalid_value"
    try:
        volumes = parse_volumes(sample_input)
        print(volumes)
    except ValueError as e:
        print(f"Error: {e}")
    
    valid_input = "5.5, 10, 15.75"
    valid_volumes = parse_volumes(valid_input)
    print(valid_volumes)