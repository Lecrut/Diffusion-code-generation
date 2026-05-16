def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
if __name__ == '__main__':
    sample_temperatures = [20, 37, 0, 100, -40, 50]
    print("Celsius to Fahrenheit Conversion Results:")
    for celsius in sample_temperatures:
        try:
            celsius_float = float(celsius)
            fahrenheit = convert_celsius_to_fahrenheit(celsius_float)
            print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
        except ValueError:
            print(f"Invalid input encountered for value: {celsius}")