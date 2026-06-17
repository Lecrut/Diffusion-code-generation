def convert_temperature(temp: float) -> tuple[float, float]:
    return temp * 9 / 5 + 32, (temp - 32) * 5 / 9
if __name__ == '__main__':
    test_values = [0.0, 100.0]
    for t in test_values:
        celsius = convert_temperature(t)[0]
        fahrenheit = convert_temperature(t)[1]
        print(f"{t}°C -> {celsius:.2f}°F")