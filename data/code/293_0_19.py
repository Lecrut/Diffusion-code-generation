def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

if __name__ == '__main__':
    temp_c = 25
    temp_f = 70
    
    print(f"{temp_c}°C is {celsius_to_fahrenheit(temp_c)}°F")
    print(f"{temp_f}°F is {fahrenheit_to_celsius(temp_f)}°C")