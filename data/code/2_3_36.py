def parse_volume_values(volume_string):
    try:
        volume_list = [float(value.strip()) for value in volume_string.split(',')]
        return volume_list
    except ValueError as e:
        raise ValueError("Invalid input: All values must be numeric.") from e

if __name__ == '__main__':
    sample_input = "3.14, 2.71, 1.41, invalid"
    try:
        result = parse_volume_values(sample_input)
        print(result)
    except ValueError as e:
        print(e)