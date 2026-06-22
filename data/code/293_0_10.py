C_TO_F_FACTOR = 9 / 5
C_TO_F_OFFSET = 32
F_TO_C_FACTOR = 5 / 9
F_TO_C_OFFSET = -32

def celsius_to_fahrenheit(c):
    return C_TO_F_FACTOR * c + C_TO_F_OFFSET

def fahrenheit_to_celsius(f):
    return F_TO_C_FACTOR * (f + F_TO_C_OFFSET)
if __name__ == '__main__':
    print(celsius_to_fahrenheit(0))
    print(fahrenheit_to_celsius(32))