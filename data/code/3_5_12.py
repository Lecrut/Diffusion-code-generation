def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

if __name__ == '__main__':
    sample_celsius = 25.0
    sample_fahrenheit = 77.0
    sample_kelvin = 300.0

    f_result = celsius_to_fahrenheit(sample_celsius)
    c_from_f = fahrenheit_to_celsius(sample_fahrenheit)
    c_from_k = kelvin_to_celsius(sample_kelvin)

    print(f_result)
    print(c_from_f)
    print(c_from_k)