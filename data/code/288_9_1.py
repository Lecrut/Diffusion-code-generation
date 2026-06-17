def convert_temperature(celsius: float, target_unit: str) -> float:
    if target_unit.lower() == 'fahrenheit':
        return (celsius * 9/5) + 32
    elif target_unit.lower() == 'kelvin':
        return celsius + 273.15
    elif target_unit.lower() == 'celsius':
        return celsius
    else:
        raise ValueError("Unsupported target unit. Must be 'Celsius', 'Fahrenheit', or 'Kelvin'.")
if __name__ == '__main__':
    sample_celsius = 25.0
    sample_fahrenheit = 77.0
    sample_kelvin = 298.15
    result_f = convert_temperature(sample_celsius, 'Fahrenheit')
    result_k = convert_temperature(sample_celsius, 'Kelvin')
    result_c = convert_temperature(sample_celsius, 'Celsius')
    result_f2 = convert_temperature(sample_fahrenheit, 'Celsius')
    result_k2 = convert_temperature(sample_kelvin, 'Kelvin')
    print(f"25.0 Celsius to Fahrenheit: {result_f}")
    print(f"25.0 Celsius to Kelvin: {result_k}")
    print(f"25.0 Celsius to Celsius: {result_c}")
    print(f"77.0 Fahrenheit to Celsius: {result_f2}")
    print(f"298.15 Kelvin to Kelvin: {result_k2}")