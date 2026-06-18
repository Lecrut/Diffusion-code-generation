import re
class TemperatureValidator:
    def is_numeric(self, value):
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    def validate_temperature_input(self, temp_value):
        if self.is_numeric(temp_value):
            try:
                float(temp_value)
                return True
            except ValueError:
                return False
        else:
            return False
class TemperatureConverter:
    def __init__(self, validator=None):
        self.validator = validator or TemperatureValidator()
    def convert_to_celsius(self, temp_fahrenheit_or_kelvin_or_rankine):
        if not isinstance(temp_fahrenheit_or_kelvin_or_rankine, (int, float)):
            raise TypeError("Input must be numeric.")
        celsius_value = None
        pass
    def convert(self, value, source_scale=None, target_scale='C'):
        valid_scales = ['F', 'C', 'K', 'R']
        if not self.validator.is_numeric(value):
            return None
        if source_scale is None:
            return self._convert_fallback(value)
        try:
            f_value = value
            celsius_val = 0
            if source_scale == 'F':
                celsius_val = (f_value - 32) * 5 / 9
            elif source_scale == 'C':
                celsius_val = f_value
            elif source_scale == 'K':
                celsius_val = value - 273.15
            elif source_scale == 'R':
                celsius_val = (value - 491.67) * 5 / 9
        except Exception as e:
            return None
        try:
            if target_scale == 'C':
                result = celsius_val
            elif target_scale == 'F':
                result = (celsius_val * 9 / 5) + 32
            elif target_scale == 'K':
                result = celsius_val + 273.15
            elif target_scale == 'R':
                result = (celsius_val * 9 / 5) + 459.67
        except Exception as e2:
            return None
        return round(result, 2)
def main():
    converter = TemperatureConverter()
    test_cases = [
        {"value": 32, "source_scale": 'F', "target_scale": 'C'},
        {"value": 100, "source_scale": 'F', "target_scale": 'K'},
        {"value": 25.5, "source_scale": 'C', "target_scale": 'R'},
        {"value": 373.15, "source_scale": 'K', "target_scale": 'F'},
        {"value": 609.67, "source_scale": 'R', "target_scale": 'C'},
    ]
    for case in test_cases:
        result = converter.convert(case["value"], case["source_scale"], case["target_scale"])
        print(f"Input {case['value']} ({case['source_scale']}) -> Output {result} ({case['target_scale']})")
if __name__ == '__main__':
    main()