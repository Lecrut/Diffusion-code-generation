def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

if __name__ == '__main__':
    c_val = 100
    f_val = 32
    k_val = 0

    f_result = celsius_to_fahrenheit(c_val)
    c_from_f = fahrenheit_to_celsius(f_val)
    c_from_k = kelvin_to_celsius(k_val)

    print(f_result)
    print(c_from_f)
    print(c_from_k)