def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

if __name__ == '__main__':
    temp1 = 300
    temp2 = 290
    difference = kelvin_to_celsius(temp1) - kelvin_to_celsius(temp2)
    print(difference)