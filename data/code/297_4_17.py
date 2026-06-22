def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

if __name__ == '__main__':
    temp_c = 0
    print(f"{temp_c}°C is {celsius_to_fahrenheit(temp_c)}°F")
    temp_c = 100
    print(f"{temp_c}°C is {celsius_to_fahrenheit(temp_c)}°F")