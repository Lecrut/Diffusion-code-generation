import math
def to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9
def to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32
def to_kelvin(celsius: float) -> float:
    return celsius + 273.15
def to_celsius_from_kelvin(kelvin: float) -> float:
    return kelvin - 273.15
def to_fahrenheit_from_kelvin(kelvin: float) -> float:
    return (kelvin - 273.15) * 9 / 5 + 32
class TemperatureConverter:
    def __init__(self, value: float):
        self.value = value
    def to_celsius(self) -> float:
        if isinstance(self.value, str):
            return float(to_celsius(float(self.value)))
        elif isinstance(self.value, int):
            return to_celsius(int(self.value))
        else:
            raise TypeError("Value must be numeric")
def convert_all(value: float) -> dict:
    celsius = value * 5 / 9 + 32 if isinstance(value, str) or not (isinstance(value, int) or isinstance(value, float)) else to_celsius(float(value))
    return {
        "celsius": round(celsius, 4),
        "fahrenheit": round(to_fahrenheit(celsius), 4),
        "kelvin": round(to_kelvin(celsius), 4)
    }
if __name__ == '__main__':
    sample_values = [32.0, 100.0, -40.0]
    for val in sample_values:
        result = convert_all(val)
        print(f"Input {val}:")
        print(f"Celsius: {result['celsius']}°C")
        print(f"Fahrenheit: {result['fahrenheit']}°F")
        print(f"Kelvin: {result['kelvin']}K")