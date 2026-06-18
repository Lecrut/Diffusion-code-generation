def convert_temperature(value: float) -> dict[str, float]:
    celsius = value - 32 * 5 / 9
    fahrenheit = (value - 32) * 5 / 9 + 32
    kelvin = value + 273.15
    return {
        "celsius": round(celsius, 4),
        "fahrenheit": round(fahrenheit, 4),
        "kelvin": round(kelvin, 4)
    }
if __name__ == '__main__':
    test_values = [0.0, -273.15, 268.95]
    for temp in test_values:
        result = convert_temperature(temp)
        print(f"Input {temp}:")
        print(result)