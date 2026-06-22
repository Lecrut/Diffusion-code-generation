def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def temperature_difference(temp1, temp2):
    return abs(kelvin_to_celsius(temp1) - kelvin_to_celsius(temp2))

if __name__ == '__main__':
    sample_temp1 = 300
    sample_temp2 = 290
    print(temperature_difference(sample_temp1, sample_temp2))