def parse_volume_values(volume_string):
    try:
        return [float(value.strip()) for value in volume_string.split(',')]
    except ValueError as e:
        raise ValueError(f"Error parsing volume values: {e}")

if __name__ == '__main__':
    sample_input = "1.5, 2.3, 3.7, four"
    try:
        parsed_values = parse_volume_values(sample_input)
        print(parsed_values)
    except ValueError as e:
        print(e)