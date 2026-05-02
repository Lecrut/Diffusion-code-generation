import sys
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
if __name__ == '__main__':
    sample_temperatures = [20, 37, 0, 100, -40, 98.6]
    print("Celsius to Fahrenheit Conversion Results:")
    for celsius in sample_temperatures:
        if isinstance(celsius, (int, float)):
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Celsius: {celsius}°C, Fahrenheit: {fahrenheit:.2f}°F")
        else:
            print(f"Invalid input encountered: {celsius}")