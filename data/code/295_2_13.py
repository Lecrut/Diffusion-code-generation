def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return int(celsius)

if __name__ == '__main__':
    sample_fahrenheit = 68
    converted_celsius = fahrenheit_to_celsius(sample_fahrenheit)
    print(converted_celsius)