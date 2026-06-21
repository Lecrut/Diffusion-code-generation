def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_temperatures(temperature_dict):
    converted_dict = {}
    for location, temp in temperature_dict.items():
        fahrenheit_temp = celsius_to_fahrenheit(temp)
        converted_dict[location] = fahrenheit_temp
    return converted_dict

if __name__ == '__main__':
    sample_temperatures = {
        'Paris': 5,
        'London': 12,
        'Rome': 8
    }
    converted_temperatures = convert_temperatures(sample_temperatures)
    print(converted_temperatures)