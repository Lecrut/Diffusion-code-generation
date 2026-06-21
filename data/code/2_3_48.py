def parse_volume_values(volume_string):
    volume_list = []
    for value in volume_string.split(','):
        try:
            float_value = float(value.strip())
            volume_list.append(float_value)
        except ValueError:
            raise ValueError(f"Invalid numeric value: {value}")
    return volume_list

if __name__ == '__main__':
    sample_input = "3.14, 2.718, abc, 0.99"
    try:
        result = parse_volume_values(sample_input)
        print(result)
    except ValueError as e:
        print(e)