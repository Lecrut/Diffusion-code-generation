VOLUME_SEPARATOR = ','

def parse_volume_values(volume_string):
    try:
        volume_list = [float(value.strip()) for value in volume_string.split(VOLUME_SEPARATOR)]
        return volume_list
    except ValueError as e:
        raise ValueError("Invalid input: All values must be numeric.") from e

if __name__ == '__main__':
    sample_input_1 = "3.14, 2.71, 0.98, 1.41"
    try:
        result_1 = parse_volume_values(sample_input_1)
        print("Parsed volumes:", result_1)
    except ValueError as e:
        print(e)

    sample_input_2 = "3.14, 2.71, 1.41, invalid"
    try:
        result_2 = parse_volume_values(sample_input_2)
        print("Parsed volumes:", result_2)
    except ValueError as e:
        print(e)

    sample_input_3 = "3.14, 2.71, 0.98, 1.618"
    try:
        result_3 = parse_volume_values(sample_input_3)
        print("Parsed volumes:", result_3)
    except ValueError as e:
        print(e)

    sample_input_4 = "3.5, 4.2, 7.8, invalid"
    try:
        result_4 = parse_volume_values(sample_input_4)
        print("Parsed volumes:", result_4)
    except ValueError as e:
        print(e)