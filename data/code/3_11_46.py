def celsius_to_fahrenheit(celsius_list):
    def validate_temperature(temp):
        if not isinstance(temp, (int, float)):
            raise ValueError(f"Invalid temperature value: {temp}. Must be an integer or float.")
    
    validated_temperatures = [validate_temperature(c) for c in celsius_list]
    conversion_factor = 9 / 5
    base_temperature = 32
    return [c * conversion_factor + base_temperature for c in celsius_list]

if __name__ == '__main__':
    sample_temperatures = [-40, 0, 100, 37]
    try:
        fahrenheit_temperatures = celsius_to_fahrenheit(sample_temperatures)
        print(fahrenheit_temperatures)
    except ValueError as e:
        print(e)