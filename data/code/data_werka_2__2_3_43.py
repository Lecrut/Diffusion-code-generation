def parse_volume_values(volume_string):
    def convert_to_float(value):
        try:
            return float(value.strip())
        except ValueError:
            raise ValueError(f"Invalid input: '{value}' is not a numeric value.")
    
    volume_list = []
    for value in volume_string.split(','):
        try:
            number = convert_to_float(value)
            volume_list.append(number)
        except ValueError as e:
            print(e)
    
    return volume_list

if __name__ == '__main__':
    sample_input = "5.0, 2.5, 3.14, not_a_number"
    result = parse_volume_values(sample_input)
    print(result)