def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

if __name__ == '__main__':
    sample_f = 100
    sample_c = 0
    print(f"{sample_f}F is {fahrenheit_to_celsius(sample_f)}C")
    print(f"{sample_c}C is {celsius_to_fahrenheit(sample_c)}F")