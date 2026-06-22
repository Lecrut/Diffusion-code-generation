def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

if __name__ == '__main__':
    temp_c = 10
    temp_f = celsius_to_fahrenheit(temp_c)
    print(f"{temp_c}°C is {temp_f}°F")

    temp_f = 50
    temp_c = fahrenheit_to_celsius(temp_f)
    print(f"{temp_f}°F is {temp_c}°C")