def is_valid_temperature(value):
    return isinstance(value, float)

def celsius_to_fahrenheit(celsius):
    if not is_valid_temperature(celsius):
        raise ValueError("Invalid input. Please provide a valid floating-point number.")
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    if not is_valid_temperature(fahrenheit):
        raise ValueError("Invalid input. Please provide a valid floating-point number.")
    return (fahrenheit - 32) * 5/9

if __name__ == '__main__':
    c_temp = 25.0
    f_temp = celsius_to_fahrenheit(c_temp)
    print(f"{c_temp}°C is {f_temp:.2f}°F")

    f_temp = 77.0
    c_temp = fahrenheit_to_celsius(f_temp)
    print(f"{f_temp}°F is {c_temp:.2f}°C")