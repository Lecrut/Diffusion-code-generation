def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit

if __name__ == '__main__':
    temp_fahrenheit = 100
    temp_celsius = -40
    
    print(f"{temp_fahrenheit}°F is {fahrenheit_to_celsius(temp_fahrenheit):.2f}°C")
    print(f"{temp_celsius}°C is {celsius_to_fahrenheit(temp_celsius):.2f}°F")