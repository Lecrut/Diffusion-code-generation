def validate_temperature(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Temperature must be a number")

def celsius_to_fahrenheit(celsius):
    validate_temperature(celsius)
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    validate_temperature(fahrenheit)
    return (fahrenheit - 32) * 5/9

if __name__ == '__main__':
    celsius_temp = 25.0
    fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
    print(f"{celsius_temp}°C is {fahrenheit_temp:.2f}°F")

    fahrenheit_temp = 77.0
    celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
    print(f"{fahrenheit_temp}°F is {celsius_temp:.2f}°C")