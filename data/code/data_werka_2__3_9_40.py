def kelvin_to_celsius(kelvin_list):
    celsius_list = []
    for temp in kelvin_list:
        if temp < 0:
            raise ValueError("Temperature cannot be below absolute zero.")
        celsius_temp = temp - 273.15
        celsius_list.append(celsius_temp)
    return celsius_list

if __name__ == '__main__':
    sample_kelvin_temps = [0, 273.15, 300, 500]
    converted_temps = kelvin_to_celsius(sample_kelvin_temps)
    print(converted_temps)