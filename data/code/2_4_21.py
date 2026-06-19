def parse_volume_values(volume_string):
    try:
        volume_list = [float(value.strip()) for value in volume_string.split(',')]
        return volume_list
    except ValueError:
        raise ValueError("Input contains non-numeric values")

if __name__ == '__main__':
    sample_input = "10.5, 20.3, 30.7"
    try:
        result = parse_volume_values(sample_input)
        print(result)
    except ValueError as e:
        print(e)