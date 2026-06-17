import math
class TemperatureConverter:
    def _validate_numeric(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a numeric type.")
        try:
            num = float(value)
        except ValueError:
            raise ValueError("Input temperature is not valid.")
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
    c_temp = 25.0
    f_result = converter.celsius_to_fahrenheit(c_temp)
    k_result = converter.celsius_to_kelvin(c_temp)
    print(f"Celsius ({c_temp}) -> Fahrenheit: {f_result}")
    print(f"Celsius ({c_temp}) -> Kelvin: {k_result}")
    f_input = 68.0
    r_input = 527.34
    c_from_f = converter.fahrenheit_to_celsius(f_input)
    k_from_r = converter.rankine_to_kelvin(r_input) if hasattr(converter, 'rankine_to_kelvin') else None
    def r_to_k(temp):
        return (temp - 459.67) + 273.15
    k_from_r = r_to_k(r_input) if isinstance(r_input, float) else None
    print(f"Fahrenheit ({f_input}) -> Celsius: {c_from_f}")
    r_to_k_direct = (r_input - 459.67) + 273.15 if isinstance(r_input, float) else None
    print(f"Rankine ({r_input}) -> Kelvin: {k_from_r}")
    try:
        converter.celsius_to_fahrenheit("invalid")
    except (TypeError, ValueError):
        pass