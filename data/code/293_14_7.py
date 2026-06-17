import math
def meters_to_feet(meters: float) -> float:
    return meters * 3.28084
def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32
if __name__ == '__main__':
    meter_value = 10.0
    feet_value = meters_to_feet(meter_value)
    print(f"{meter_value} meters is equal to {feet_value:.2f} feet")
    celsius_value = 25.0
    fahrenheit_value = celsius_to_fahrenheit(celsius_value)
    print(f"{celsius_value}°C is equal to {fahrenheit_value:.2f}°F")