def convert_temperature(celsius: float) -> tuple[float, float]:
    fahrenheit = celsius * 9 / 5 + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin
if __name__ == '__main__':
    sample_temperatures: list[float] = [0.0, 100.0, -40.0, 25.5]
    for temp in sample_temperatures:
        fah, kel = convert_temperature(temp)
        print(f"{temp}°C -> {fah:.2f}°F ({kel:.2f}K)")