def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32
if __name__ == '__main__':
    print(fahrenheit_to_celsius(32))
    print(fahrenheit_to_celsius(212))
    print(celsius_to_fahrenheit(0))
    print(celsius_to_fahrenheit(100))