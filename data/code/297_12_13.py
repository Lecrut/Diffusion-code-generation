FAHRENHEIT_TO_CELSIUS = 5/9
CELSIUS_TO_FAHRENHEIT = 9/5

def fahrenheit_to_celsius(f):
    return (f - 32) * FAHRENHEIT_TO_CELSIUS

def celsius_to_fahrenheit(c):
    return c * CELSIUS_TO_FAHRENHEIT + 32

if __name__ == '__main__':
    temp_f = -40
    print(f"{temp_f}°F is {fahrenheit_to_celsius(temp_f)}°C")
    temp_c = -40
    print(f"{temp_c}°C is {celsius_to_fahrenheit(temp_c)}°F")