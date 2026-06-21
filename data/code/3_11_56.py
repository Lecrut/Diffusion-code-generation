def convert_celsius_to_fahrenheit(celsius_list):
    fahrenheit_list = []
    for celsius in celsius_list:
        if not isinstance(celsius, (int, float)):
            raise ValueError("Temperature must be an integer or float.")
        fahrenheit = celsius * 9/5 + 32
        fahrenheit_list.append(fahrenheit)
    return fahrenheit_list

if __name__ == '__main__':
    sample_temperatures = [25, -10, 100, 40]
    try:
        fahrenheit_temperatures = convert_celsius_to_fahrenheit(sample_temperatures)
        print(fahrenheit_temperatures)
    except ValueError as e:
        print(e)