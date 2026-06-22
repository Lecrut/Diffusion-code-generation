C_TO_F_FACTOR = 9 / 5
C_TO_F_OFFSET = 32

def celsius_to_fahrenheit(c):
    return c * C_TO_F_FACTOR + C_TO_F_OFFSET

F_TO_C_FACTOR = 5 / 9
F_TO_C_OFFSET = -C_TO_F_OFFSET / F_TO_C_FACTOR

def fahrenheit_to_celsius(f):
    return (f - C_TO_F_OFFSET) * F_TO_C_FACTOR

if __name__ == '__main__':
    print(celsius_to_fahrenheit(0))
    print(fahrenheit_to_celsius(32))