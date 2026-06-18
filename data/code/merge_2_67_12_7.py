import math
class TemperatureConverter:
    def _validate_numeric(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a numeric type.")
        try:
            num = float(value)
        except ValueError:
            raise ValueError("Input temperature is not valid.")
        return num
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
    def fahrenheit_to_rankine(self, temp_f):
        self._validate_numeric(temp_f)
        return temp_f + 459.67
    def rankine_to_fahrenheit(self, temp_r):
        self._validate_numeric(temp_r)
        return temp_r - 459.67
if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius = 25.0
    sample_fahrenheit = 77.0
    sample_kelvin = 300.0
    sample_rankine = 80.0
    print(f"Celsius to Fahrenheit: {converter.celsius_to_fahrenheit(sample_celsius)}")
    print("Fahrenheit to Celsius:", converter.fahrenheit_to_celsius(sample_fahrenheit))
    print("Celsius to Kelvin:", converter.celsius_to_kelvin(sample_celsius))
    print("Kelvin to Celsius:", converter.kelvin_to_celsius(sample_kelvin))
    print(f"Fahrenheit to Rankine: {converter.fahrenheit_to_rankine(sample_fahrenheit)}")
    print("Rankine to Fahrenheit:", converter.rankine_to_fahrenheit(sample_rankine))
    try:
        invalid_input = "not a number"
        result = converter.celsius_to_kelvin(invalid_input)
    except (TypeError, ValueError):
        print(f"Error handling for '{invalid_input}': Exception raised as expected.")