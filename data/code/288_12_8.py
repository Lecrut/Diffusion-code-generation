def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kelvin_to_celsius(k):
    return k - 273.15

def average_temperature(temp1, scale1, temp2, scale2, temp3, scale3):
    if scale1 == 'C':
        c1 = temp1
    elif scale1 == 'F':
        c1 = fahrenheit_to_celsius(temp1)
    else:
        c1 = kelvin_to_celsius(temp1)

    if scale2 == 'C':
        c2 = temp2
    elif scale2 == 'F':
        c2 = fahrenheit_to_celsius(temp2)
    else:
        c2 = kelvin_to_celsius(temp2)

    if scale3 == 'C':
        c3 = temp3
    elif scale3 == 'F':
        c3 = fahrenheit_to_celsius(temp3)
    else:
        c3 = kelvin_to_celsius(temp3)

    return (c1 + c2 + c3) / 3

if __name__ == '__main__':
    print(average_temperature(0, 'C', 32, 'F', 273.15, 'K'))