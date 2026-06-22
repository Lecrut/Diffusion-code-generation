def validate_temperature(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Invalid temperature value")

def celsius_to_fahrenheit(c):
    validate_temperature(c)
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    validate_temperature(f)
    return (f - 32) * 5 / 9

if __name__ == '__main__':
    print(celsius_to_fahrenheit(0))
    print(fahrenheit_to_celsius(32))