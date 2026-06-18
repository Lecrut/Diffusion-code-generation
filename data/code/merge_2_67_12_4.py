import sys
def validate_temperature(value):
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False
class TemperatureConverter:
    def __init__(self, value):
        self.value = value
    def to_celsius(self):
        if not isinstance(self.value, (int, float)):
            raise ValueError("Input must be numeric")
        celsius = (self.value - 32) * 5 / 9
        return round(celsius, 4)
    def to_fahrenheit(self):
        if not isinstance(self.value, (int, float)):
            raise ValueError("Input must be numeric")
        fahrenheit = self.value * 9 / 5 + 32
        return round(fahrenheit, 4)
    def to_kelvin(self):
        if not isinstance(self.value, (int, float)):
            raise ValueError("Input must be numeric")
        kelvin = self.value - 273.15
        return round(kelvin, 4)
    def to_rankine(self):
        if not isinstance(self.value, (int, float)):
            raise ValueError("Input must be numeric")
        rankine = (self.value + 459.67) * 9 / 5
        return round(rankine, 4)
if __name__ == '__main__':
    sample_values = [32, -10, "invalid", None]
    for val in sample_values:
        if isinstance(val, str):
            continue
        converter_instance = TemperatureConverter(val)
        try:
            celsius_result = converter_instance.to_celsius()
            fahrenheit_result = converter_instance.to_fahrenheit()
            kelvin_result = converter_instance.to_kelvin()
            rankine_result = converter_instance.to_rankine()
            print(f"Input: {val}")
            print(f"Celsius: {celsius_result}, Fahrenheit: {fahrenheit_result}")
            print(f"Kelvin: {kelvin_result}, Rankine: {rankine_result}\n")
        except Exception as e:
            print(f"Error processing input '{val}': {e}\n", file=sys.stderr)