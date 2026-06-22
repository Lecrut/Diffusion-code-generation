def fahrenheit_to_celsius(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError('Input must be a number')
    return int((fahrenheit - 32) * 5 / 9)
if __name__ == '__main__':
    print(fahrenheit_to_celsius(32))
    print(fahrenheit_to_celsius(212))
    print(fahrenheit_to_celsius(-40))