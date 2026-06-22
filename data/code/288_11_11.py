def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def temperature_difference(temp1, temp2):
    return abs(kelvin_to_celsius(temp1) - kelvin_to_celsius(temp2))

if __name__ == '__main__':
    result = temperature_difference(300, 290)
    print(result)