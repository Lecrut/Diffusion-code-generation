def convert_celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise ValueError("Temperature must be a number")
    return (celsius * 9/5) + 32

if __name__ == '__main__':
    temperatures = [0, -40, 100, 25, 20]
    max_celsius = max(temperatures)
    max_fahrenheit = convert_celsius_to_fahrenheit(max_celsius)
    print(f"Maximum temperature in Fahrenheit: {max_fahrenheit}")