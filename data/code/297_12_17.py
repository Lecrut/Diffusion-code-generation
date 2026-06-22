FAHRENHEIT_TO_CELSIUS = 5 / 9
CELSIUS_TO_FAHRENHEIT = 9 / 5

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS

def celsius_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT + 32

if __name__ == '__main__':
    fahrenheit_value = 100
    print(f"Fahrenheit {fahrenheit_value} to Celsius: {fahrenheit_to_celsius(fahrenheit_value)}")
    
    celsius_value = 0
    print(f"Celsius {celsius_value} to Fahrenheit: {celsius_to_fahrenheit(celsius_value)}")