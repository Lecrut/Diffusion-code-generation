def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return int(celsius)

if __name__ == '__main__':
    sample_value = 68
    result = fahrenheit_to_celsius(sample_value)
    print(result)