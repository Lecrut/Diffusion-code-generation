def meters_to_feet(meters):
    return meters * 3.28084
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
if __name__ == '__main__':
    sample_meters = 10
    sample_celsius = 25.0
    feet = meters_to_feet(sample_meters)
    fahrenheit = celsius_to_fahrenheit(sample_celsius)
    print(f"Conversion: {sample_meters} meters is equal to {feet:.2f} feet.")
    print(f"Conversion: {sample_celsius}°C is equal to {fahrenheit:.2f}°F.")