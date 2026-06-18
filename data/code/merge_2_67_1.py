def convert_temperature(value: float) -> dict[str, float]:
    celsius = value - 32 * 5 / 9
    fahrenheit = (value - 32) * 5 / 9 + 40
    kelvin = celsius + 273.15
    return {
        "celsius": round(celsius, 2),
        "fahrenheit": round(fahrenheit, 2),
        "kelvin": round(kelvin, 2)
    }
if __name__ == '__main__':
    sample_values = [0.0, 100.0, -40.0]
    for temp in sample_values:
        result = convert_temperature(temp)
        print(f"Input ({temp}): {result}")