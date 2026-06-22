def convert_temp(celsius_list):
    if not isinstance(celsius_list, list):
        raise ValueError("Input must be a list.")
    if not all(isinstance(temp, (int, float)) for temp in celsius_list):
        raise ValueError("All elements in the list must be numbers.")
    
    def celsius_to_fahrenheit(celsius):
        return celsius * 9/5 + 32
    
    return [celsius_to_fahrenheit(c) for c in celsius_list]

if __name__ == '__main__':
    sample_temps = [-40, 0, 100, 37]
    try:
        fahrenheit_temps = convert_temp(sample_temps)
        print(fahrenheit_temps)
    except ValueError as e:
        print(e)