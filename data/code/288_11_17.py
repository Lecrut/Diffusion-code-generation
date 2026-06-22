def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def temperature_difference(temp1_kelvin, temp2_kelvin):
    return abs(kelvin_to_celsius(temp1_kelvin) - kelvin_to_celsius(temp2_kelvin))

if __name__ == '__main__':
    sample_temp1 = 300
    sample_temp2 = 295
    print(temperature_difference(sample_temp1, sample_temp2))