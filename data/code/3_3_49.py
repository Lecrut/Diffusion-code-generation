def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    if kelvin < 0:
        raise ValueError("Kelvin temperature cannot be below absolute zero")
    return kelvin - 273.15

if __name__ == '__main__':
    celsius = 25
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}C is {fahrenheit}F")

    fahrenheit = 77
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}F is {celsius}C")

    kelvin = 300
    celsius = kelvin_to_celsius(kelvin)
    print(f"{kelvin}K is {celsius}C")