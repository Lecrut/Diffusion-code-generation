def fahrenheit_to_celsius(f):
    return int((f - 32) * 5 / 9)
if __name__ == '__main__':
    print(fahrenheit_to_celsius(32))
    print(fahrenheit_to_celsius(212))