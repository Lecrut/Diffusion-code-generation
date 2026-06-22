FAHRENHEIT_TO_CELSIUS = 5 / 9
CELSIUS_OFFSET = -32

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit + CELSIUS_OFFSET) * FAHRENHEIT_TO_CELSIUS
    return int(celsius)
if __name__ == '__main__':
    print(fahrenheit_to_celsius(32))
    print(fahrenheit_to_celsius(212))