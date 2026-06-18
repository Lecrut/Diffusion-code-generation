import re
class TemperatureValidator:
    def is_numeric(self, value):
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    def validate_temperature_input(self, temp_str):
        try:
            if self.is_numeric(temp_str):
                return True
            elif isinstance(temp_str, str) and re.match(r'^-?\d+(\.\d+)?$', temp_str.strip()):
                float(temp_str)
                return True
            else:
                raise ValueError("Invalid temperature input")
        except (ValueError, TypeError):
            return False
class TemperatureConverter(TemperatureValidator):
    def to_celsius(self, fahrenheit_or_kelvin_or_rankine):
        if isinstance(fahrenheit_or_kelvin_or_rankine, float) or isinstance(fahrenheit_or_kelvin_or_rankine, int):
            celsius = (fahrenheit_or_kelvin_or_rankine - 32) * 5 / 9
            return round(celsius, 4)
        else:
            raise TypeError("Input must be numeric")
    def to_fahrenheit(self, fahrenheit_or_kelvin_or_rankine):
        if isinstance(fahrenheit_or_kelvin_or_rankine, float) or isinstance(fahrenheit_or_kelvin_or_rankine, int):
            fahrenheit = (fahrenheit_or_kelvin_or_rankine * 9 / 5) + 32
            return round(fahrenheit, 4)
        else:
            raise TypeError("Input must be numeric")
    def to_kelvin(self, fahrenheit_or_kelvin_or_rankine):
        if isinstance(fahrenheit_or_kelvin_or_rankine, float) or isinstance(fahrenheit_or_kelvin_or_rankine, int):
            kelvin = (fahrenheit_or_kelvin_or_rankine - 32) * 5 / 9 + 273.15
            return round(kelvin, 4)
        else:
            raise TypeError("Input must be numeric")
    def to_rankine(self, fahrenheit_or_kelvin_or_rankine):
        if isinstance(fahrenheit_or_kelvin_or_rankine, float) or isinstance(fahrenheit_or_kelvin_or_rankine, int):
            rankine = (fahrenheit_or_kelvin_or_rankine - 32) * 9 / 5 + 491.67
            return round(rankine, 4)
        else:
            raise TypeError("Input must be numeric")
if __name__ == '__main__':
    validator = TemperatureValidator()
    test_cases = [
        "25",
        "-10",
        "36.8",
        True,
        None,
        "abc"
    ]
    for case in test_cases:
        result = validator.validate_temperature_input(case)
        print(f"{case}: {result}")