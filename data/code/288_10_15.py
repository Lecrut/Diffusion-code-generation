def validate_temperature(value):
    if not isinstance(value, int) or value < -273:
        raise ValueError('Temperature must be an integer and not below absolute zero')

def celsius_to_fahrenheit(celsius):
    validate_temperature(celsius)
    return celsius * 9 // 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    validate_temperature(fahrenheit)
    return (fahrenheit - 32) * 5 // 9
if __name__ == '__main__':
    sample_celsius = 25
    print(celsius_to_fahrenheit(sample_celsius))
    sample_fahrenheit = 77
    print(fahrenheit_to_celsius(sample_fahrenheit))