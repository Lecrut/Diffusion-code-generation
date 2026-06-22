def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

if __name__ == '__main__':
    temp_c = 25
    temp_f = 77
    
    print(f"Celsius {temp_c} to Fahrenheit: {celsius_to_fahrenheit(temp_c)}")
    print(f"Fahrenheit {temp_f} to Celsius: {fahrenheit_to_celsius(temp_f)}")