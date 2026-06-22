FAHRENHEIT_OFFSET = 32
FAHRENHEIT_FACTOR = 9 / 5

def celsius_to_fahrenheit(celsius):
    return int(celsius * FAHRENHEIT_FACTOR + FAHRENHEIT_OFFSET)

def fahrenheit_to_celsius(fahrenheit):
    return int((fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_FACTOR ** (-1))
if __name__ == '__main__':
    sample_celsius = 25
    print(celsius_to_fahrenheit(sample_celsius))
    sample_fahrenheit = 77
    print(fahrenheit_to_celsius(sample_fahrenheit))