def parse_volume_values(volume_string):
    try:
        return [float(value.strip()) for value in volume_string.split(',')]
    except ValueError as e:
        raise ValueError("Invalid input: Non-numeric value found") from e

if __name__ == '__main__':
    sample_input = "10.5, 20.3, abc, 30.7"
    try:
        result = parse_volume_values(sample_input)
        print(result)
    except ValueError as e:
        print(e)