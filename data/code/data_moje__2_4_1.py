def parse_volume_string(input_str):
    if not input_str:
        return []
    parts = input_str.split(',')
    result = []
    for part in parts:
        stripped = part.strip()
        try:
            value = float(stripped)
            result.append(value)
        except ValueError:
            raise ValueError(f"Non-numeric value found: '{stripped}'")
    return result

if __name__ == '__main__':
    sample_input = "10.5, 20.0, 30.1, -5.5"
    print(parse_volume_string(sample_input))