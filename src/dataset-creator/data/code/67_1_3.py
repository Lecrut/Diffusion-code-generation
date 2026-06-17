def convert_temperature(value: float) -> dict[str, float]:
    celsius = (value - 32) * 5 / 9
    fahrenheit = celsius * 9 / 5 + 32
    kelvin = celsius + 273.15
    return {
        'celsius': round(celsius, 4),
        'fahrenheit': round(fahrenheit, 4),
        'kelvin': round(kelvin, 4)
    }
if __name__ == '__main__':
    sample_values = [0.0, 25.0, -10.0]
    for temp in sample_values:
        result = convert_temperature(temp)
        print(f"Input ({temp}°F):")
        print(result)