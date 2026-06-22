def convert_temp(celsius_list):
    def validate_input(temp_list):
        if not isinstance(temp_list, list):
            raise ValueError("Input must be a list.")
        if not all(isinstance(temp, (int, float)) for temp in temp_list):
            raise ValueError("All elements in the list must be numbers.")
    
    validate_input(celsius_list)
    conversion_factor = 9 / 5
    base_offset = 32
    return [c * conversion_factor + base_offset for c in celsius_list]

if __name__ == '__main__':
    sample_temps = [30, -10, 150, 25]
    try:
        fahrenheit_temps = convert_temp(sample_temps)
        print(fahrenheit_temps)
    except ValueError as e:
        print(e)