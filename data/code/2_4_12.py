def parse_volumes(volume_string):
    parts = volume_string.split(',')
    result = []
    for part in parts:
        stripped = part.strip()
        if stripped == '':
            continue
        try:
            result.append(float(stripped))
        except ValueError:
            raise ValueError(f"Non-numeric value encountered: '{stripped}'")
    return result

if __name__ == '__main__':
    sample_input = "1.5, 2.3, -4.0, 100, 0.001"
    print(parse_volumes(sample_input))
    
    try:
        invalid_input = "1.5, abc, 3.0"
        parse_volumes(invalid_input)
    except ValueError as e:
        print(e)