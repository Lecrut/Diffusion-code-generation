def parse_volumes(volume_string):
    try:
        parts = volume_string.split(',')
        result = []
        for part in parts:
            stripped = part.strip()
            if stripped == '':
                continue
            try:
                result.append(float(stripped))
            except ValueError:
                return None
        return result
    except Exception:
        return None

if __name__ == '__main__':
    sample_input = "1.5, 2.7, 3.0, invalid, 4.2"
    output = parse_volumes(sample_input)
    print(output)
    
    valid_input = "1.1, 2.2, 3.3"
    output_valid = parse_volumes(valid_input)
    print(output_valid)