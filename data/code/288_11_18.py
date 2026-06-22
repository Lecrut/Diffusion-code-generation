def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def temperature_difference(temp1, temp2):
    celsius1 = kelvin_to_celsius(temp1)
    celsius2 = kelvin_to_celsius(temp2)
    return abs(celsius1 - celsius2)

if __name__ == '__main__':
    result = temperature_difference(300, 298.15)
    print(result)