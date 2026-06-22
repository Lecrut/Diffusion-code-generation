def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

if __name__ == '__main__':
    temp_celsius = 25
    temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
    print(f"{temp_celsius}C is {temp_fahrenheit:.2f}F")

    temp_fahrenheit = 77
    temp_celsius = fahrenheit_to_celsius(temp_fahrenheit)
    print(f"{temp_fahrenheit}F is {temp_celsius:.2f}C")