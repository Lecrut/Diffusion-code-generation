import re
class TemperatureConverter:
    def _validate_numeric(self, value):
        if not isinstance(value, (int, float)):
            return False
        try:
            numeric_value = float(value)
            return True
        except ValueError:
            return False
    def convert_fahrenheit_to_celsius(self, f_temp):
        if self._validate_numeric(f_temp):
            celsius = (f_temp - 32.0) * (5.0 / 9.0)
            return round(celsius, 4)
        else:
            raise ValueError("Input must be a numeric value.")
    def convert_celsius_to_fahrenheit(self, c_temp):
        if self._validate_numeric(c_temp):
            fahrenheit = (c_temp * 9.0 / 5.0) + 32.0
            return round(fahrenheit, 4)
        else:
            raise ValueError("Input must be a numeric value.")
    def convert_fahrenheit_to_kelvin(self, f_temp):
        if self._validate_numeric(f_temp):
            kelvin = (f_temp - 32.0) * (5.0 / 9.0) + 273.15
            return round(kelvin, 4)
        else:
            raise ValueError("Input must be a numeric value.")
    def convert_kelvin_to_fahrenheit(self, k_temp):
        if self._validate_numeric(k_temp):
            fahrenheit = (k_temp - 273.15) * (9.0 / 5.0) + 32.0
            return round(fahrenheit, 4)
        else:
            raise ValueError("Input must be a numeric value.")
    def convert_fahrenheit_to_rankine(self, f_temp):
        if self._validate_numeric(f_temp):
            rankine = (f_temp - 32.0) * (9 / 5) + 491.67
            return round(rankine, 4)
        else:
            raise ValueError("Input must be a numeric value.")
    def convert_rankine_to_fahrenheit(self, r_temp):
        if self._validate_numeric(r_temp):
            fahrenheit = (r_temp - 491.67) + 32.0
            return round(fahrenheit, 4)
        else:
            raise ValueError("Input must be a numeric value.")
if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_f = 85.0
    sample_c = 21.37
    result_fc = converter.convert_fahrenheit_to_celsius(sample_f)
    print(f"{sample_f} F -> {result_fc} C")