def celsius_to_fahrenheit(celsius_list):
    conversion_factor = 9 / 5
    offset = 32
    fahrenheit_list = []
    for celsius in celsius_list:
        fahrenheit = (celsius * conversion_factor) + offset
        fahrenheit_list.append(fahrenheit)
    return fahrenheit_list

if __name__ == '__main__':
    sample_temperatures = [5, 15, 25, 35, 45]
    fahrenheit_temperatures = celsius_to_fahrenheit(sample_temperatures)
    print(fahrenheit_temperatures)