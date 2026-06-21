def kelvin_to_celsius(kelvin_list):
    celsius_list = []
    for temp in kelvin_list:
        if temp < 0:
            raise ValueError("Temperature in Kelvin cannot be negative")
        celsius_temp = temp - 273.15
        celsius_list.append(celsius_temp)
    return celsius_list

if __name__ == '__main__':
    sample_kelvin_values = [0, 273.15, 300, 500]
    converted_celsius_values = kelvin_to_celsius(sample_kelvin_values)
    print(converted_celsius_values)