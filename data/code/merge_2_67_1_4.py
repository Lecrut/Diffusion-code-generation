def convert_temperature(celsius: float) -> dict[str, float]:
    fahrenheit = celsius * 9 / 5 + 32
    kelvin = celsius + 273.15
    return {
        "celsius": round(celsius, 4),
        "fahrenheit": round(fahrenheit, 4),
        "kelvin": round(kelvin, 4)
    }
if __name__ == '__main__':
    sample_temps = [0.0, 25.0, -10.0]
    for temp in sample_temps:
        result = convert_temperature(temp)
        print(f"Celsius: {result['celsius']}")
        print(f"Fahrenheit: {result['fahrenheit']}")
        print(f"Kelvin: {result['kelvin']}\n")