def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kelvin_to_celsius(k):
    return k - 273.15

def average_temperature(temp1, scale1, temp2, scale2, temp3, scale3):
    if scale1 == 'C':
        temp1 = fahrenheit_to_celsius(celsius_to_fahrenheit(temp1)) if scale1 != 'C' else temp1
    elif scale1 == 'F':
        temp1 = fahrenheit_to_celsius(temp1)
    elif scale1 == 'K':
        temp1 = kelvin_to_celsius(temp1)

    if scale2 == 'C':
        temp2 = fahrenheit_to_celsius(celsius_to_fahrenheit(temp2)) if scale2 != 'C' else temp2
    elif scale2 == 'F':
        temp2 = fahrenheit_to_celsius(temp2)
    elif scale2 == 'K':
        temp2 = kelvin_to_celsius(temp2)

    if scale3 == 'C':
        temp3 = fahrenheit_to_celsius(celsius_to_fahrenheit(temp3)) if scale3 != 'C' else temp3
    elif scale3 == 'F':
        temp3 = fahrenheit_to_celsius(temp3)
    elif scale3 == 'K':
        temp3 = kelvin_to_celsius(temp3)

    return (temp1 + temp2 + temp3) / 3

if __name__ == '__main__':
    print(average_temperature(0, 'C', 32, 'F', 273.15, 'K'))