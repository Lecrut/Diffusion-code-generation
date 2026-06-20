def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

if __name__ == '__main__':
    c_val = 0
    f_val = 32
    k_val = 273.15

    print(celsius_to_fahrenheit(c_val))
    print(fahrenheit_to_celsius(f_val))
    print(kelvin_to_celsius(k_val))