def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise ValueError("Input must be a number")
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("Input must be a number")
    return (fahrenheit - 32) * 5/9

if __name__ == '__main__':
    temp_c = 25.0
    temp_f = celsius_to_fahrenheit(temp_c)
    print(f"{temp_c}°C is {temp_f:.2f}°F")
    
    temp_f = 77.0
    temp_c = fahrenheit_to_celsius(temp_f)
    print(f"{temp_f}°F is {temp_c:.2f}°C")