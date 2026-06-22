def parse_volume_values(volume_string):
    values = volume_string.split(',')
    result = []
    for value in values:
        try:
            number = float(value)
            result.append(number)
        except ValueError:
            print(f"Warning: '{value}' is not a valid number and will be skipped.")
    return result

if __name__ == '__main__':
    sample_input = "3.14, 2.71, abc, 0.987, 5"
    parsed_values = parse_volume_values(sample_input)
    print(parsed_values)