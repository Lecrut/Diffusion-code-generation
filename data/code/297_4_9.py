def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

if __name__ == '__main__':
    sample_celsius = 0
    print(f"{sample_celsius}°C is {celsius_to_fahrenheit(sample_celsius)}°F")
    
    sample_celsius_2 = 100
    print(f"{sample_celsius_2}°C is {celsius_to_fahrenheit(sample_celsius_2)}°F")