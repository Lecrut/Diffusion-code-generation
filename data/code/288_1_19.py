def validate_temperature(temp):
    if not isinstance(temp, (int, float)) or temp < 0:
        raise ValueError("Temperature must be a non-negative number")

def convert_temp_kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def convert_temp_kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

if __name__ == '__main__':
    sample_temperature = 20
    validate_temperature(sample_temperature)
    
    celsius = convert_temp_kelvin_to_celsius(sample_temperature)
    fahrenheit = convert_temp_kelvin_to_fahrenheit(sample_temperature)
    rankine = (sample_temperature * 9/5)

    print(f"Celsius: {celsius}")
    print(f"Fahrenheit: {fahrenheit}")
    print(f"Rankine: {rankine}")