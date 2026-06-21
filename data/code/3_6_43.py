def convert_temp(celsius_list):
    if not all(isinstance(temp, (int, float)) for temp in celsius_list):
        raise ValueError("All elements in the list must be numbers.")
    
    conversion_factor = 9 / 5
    base_offset = 32
    
    return [c * conversion_factor + base_offset for c in celsius_list]

if __name__ == '__main__':
    sample_temps = [0, -40, 100, 37]
    try:
        fahrenheit_temps = convert_temp(sample_temps)
        print(fahrenheit_temps)
    except ValueError as e:
        print(e)