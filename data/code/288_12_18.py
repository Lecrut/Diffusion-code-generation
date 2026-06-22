def validate_temperature(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Temperature must be a number")

def fahrenheit_to_celsius(fahrenheit):
    validate_temperature(fahrenheit)
    return (fahrenheit - 32) * 5 / 9

def kelvin_to_celsius(kelvin):
    validate_temperature(kelvin)
    return kelvin - 273.15

def average_temperatures(celsius, fahrenheit, kelvin):
    celsius += fahrenheit_to_celsius(fahrenheit)
    celsius += kelvin_to_celsius(kelvin)
    return celsius / 3

if __name__ == '__main__':
    avg_temp = average_temperatures(25.0, 68.0, 300.15)
    print(f"The average temperature is {avg_temp}°C")