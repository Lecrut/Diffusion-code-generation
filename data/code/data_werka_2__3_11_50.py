def celsius_to_fahrenheit(celsius_list):
    return [c * 9/5 + 32 for c in celsius_list]

if __name__ == '__main__':
    sample_temperatures = [0, 10, 20, 30, 40]
    fahrenheit_temperatures = celsius_to_fahrenheit(sample_temperatures)
    print(fahrenheit_temperatures)