def celsius_to_fahrenheit(celsius_list):
    fahrenheit_list = []
    for celsius in celsius_list:
        fahrenheit = (celsius * 9/5) + 32
        fahrenheit_list.append(fahrenheit)
    return fahrenheit_list

if __name__ == '__main__':
    sample_temperatures = [10, 25, 40, 50]
    converted_temperatures = celsius_to_fahrenheit(sample_temperatures)
    print(converted_temperatures)