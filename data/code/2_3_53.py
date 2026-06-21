def parse_volume_values(volume_string):
    volume_list = []
    for value in volume_string.split(','):
        try:
            volume = float(value.strip())
            volume_list.append(volume)
        except ValueError:
            print(f"Warning: '{value}' is not a valid number and will be skipped.")
    return volume_list

if __name__ == '__main__':
    sample_input = "3.5, 4.2, invalid, 7.8"
    result = parse_volume_values(sample_input)
    print(result)