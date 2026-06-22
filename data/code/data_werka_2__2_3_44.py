def parse_volume_values(volume_string):
    def convert_to_float(value):
        try:
            return float(value.strip())
        except ValueError:
            raise ValueError(f"Invalid input: '{value}' is not a numeric value.")

    volume_list = [convert_to_float(value) for value in volume_string.split(',')]
    return volume_list

if __name__ == '__main__':
    sample_input = "3.14, 2.71, 0.98, 1.41"
    try:
        result = parse_volume_values(sample_input)
        print(result)
    except ValueError as e:
        print(e)

    invalid_sample_input = "3.14, 2.71, invalid, 1.41"
    try:
        result = parse_volume_values(invalid_sample_input)
        print(result)
    except ValueError as e:
        print(e)