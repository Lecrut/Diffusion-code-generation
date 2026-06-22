FAHRENHEIT_TO_CELSIUS = 5 / 9
CELSIUS_TO_KELVIN = 273.15
FAHRENHEIT_TO_KELVIN = FAHRENHEIT_TO_CELSIUS + CELSIUS_TO_KELVIN

def fahrenheit_to_celsius(f):
    return f * FAHRENHEIT_TO_CELSIUS

def celsius_to_kelvin(c):
    return c + CELSIUS_TO_KELVIN

def fahrenheit_to_kelvin(f):
    return f * FAHRENHEIT_TO_KELVIN

if __name__ == '__main__':
    fahrenheit_temp = 77.0
    print(f"Fahrenheit to Celsius: {fahrenheit_temp} F is {fahrenheit_to_celsius(fahrenheit_temp):.2f} C")
    print(f"Fahrenheit to Kelvin: {fahrenheit_temp} F is {fahrenheit_to_kelvin(fahrenheit_temp):.2f} K")