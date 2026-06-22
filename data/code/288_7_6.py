def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

if __name__ == '__main__':
    temperatures = [15, 28, -10, 30, 0]
    max_temp_celsius = max(temperatures)
    max_temp_fahrenheit = convert_celsius_to_fahrenheit(max_temp_celsius)
    print(f"The maximum temperature in Fahrenheit is: {max_temp_fahrenheit}")