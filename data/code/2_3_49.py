def parse_volume_values(volume_string):
    def is_valid_number(value):
        try:
            float(value.strip())
            return True
        except ValueError:
            return False

    volume_list = []
    for value in volume_string.split(','):
        if not is_valid_number(value):
            raise ValueError(f"Invalid input: '{value}' is not a numeric value.")
        volume_list.append(float(value.strip()))

    return volume_list

if __name__ == '__main__':
    sample_input = "3.14, 2.71, 0.98, 1.41"
    try:
        result = parse_volume_values(sample_input)
        print(result)
    except ValueError as e:
        print(e)

    sample_input_invalid = "3.14, 2.71, invalid, 1.41"
    try:
        result = parse_volume_values(sample_input_invalid)
        print(result)
    except ValueError as e:
        print(e)