import math
def meters_to_feet(meters: float) -> float:
    return meters * 3.28084
def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32
if __name__ == '__main__':
    meters_value = 10.0
    feet_value = meters_to_feet(meters_value)
    print(f"Conversion from {meters_value} meters to feet: {feet_value}")
    celsius_value = 25.0
    fahrenheit_value = celsius_to_fahrenheit(celsius_value)
    print(f"Conversion from {celsius_value}°C to Fahrenheit: {fahrenheit_value}°F")