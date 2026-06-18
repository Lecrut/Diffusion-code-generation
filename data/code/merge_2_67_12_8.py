import math
class TemperatureConverter:
    def _validate_numeric(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be numeric.")
        try:
            float_value = float(value)
        except ValueError:
            raise ValueError("Input cannot be converted to a number.")
        return float_value
    def celsius_to_fahrenheit(self, temp_c):
        self._validate_numeric(temp_c)
        return (temp_c * 9 / 5) + 32
    def fahrenheit_to_celsius(self, temp_f):
        self._validate_numeric(temp_f)
        return (temp_f - 32) * 5 / 9
    def celsius_to_kelvin(self, temp_c):
        self._validate_numeric(temp_c)
        return temp_c + 273.15
    def kelvin_to_celsius(self, temp_k):
        self._validate_numeric(temp_k)
        return temp_k - 273.15
    def celsius_to_rankine(self, temp_c):
        self._validate_numeric(temp_c)
        return (temp_c + 273.15) * 9 / 5
    def rankine_to_celsius(self, temp_r):
        self._validate_numeric(temp_r)
        return ((temp_r - 459.67) * 5) / 9
if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_values = {
        "c_to_f": [0, 100],
        "f_to_c": [32, 212],
        "c_to_k": [0, 100],
        "k_to_c": [273.15, 373.15],
        "c_to_r": [0, 100],
        "r_to_c": [491.67, 671.67]
    }
    for scale_name, values in sample_values.items():
        print(f"\n{scale_name}:")
        for val in values:
            if 'c' in scale_name and 'f' not in scale_name:
                result = converter.celsius_to_fahrenheit(val)
                label = "F"
            elif 'f' in scale_name and 'c' not in scale_name:
                result = converter.fahrenheit_to_celsius(val)
                label = "C"
            elif 'k' in scale_name and 'r' not in scale_name:
                result = converter.celsius_to_kelvin(val)
                label = "K"
            elif 'c' in scale_name and 'k' not in scale_name:
                result = converter.kelvin_to_celsius(val)
                label = "C"
            elif 'r' in scale_name and 'f' not in scale_name:
                result = converter.celsius_to_rankine(val)
                label = "R"
            else:
                result = converter.rankine_to_celsius(val)
                label = "C"
            print(f"{val} ({label}) -> {result}")