def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise ValueError("Input must be a number")
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("Input must be a number")
    return (fahrenheit - 32) * 5/9

if __name__ == '__main__':
    celsius_temp = 25
    fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
    print(f"{celsius_temp}°C is {fahrenheit_temp:.2f}°F")
    
    fahrenheit_temp = 77
    celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
    print(f"{fahrenheit_temp}°F is {celsius_temp:.2f}°C")