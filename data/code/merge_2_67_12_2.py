import re
class TemperatureConverter:
    def _validate_numeric(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be numeric.")
        return True
    def fahrenheit_to_celsius(self, temp_f):
        self._validate_numeric(temp_f)
        celsius = (temp_f - 32) * 5 / 9
        return round(celsius, 4)
    def fahrenheit_to_kelvin(self, temp_f):
        self._validate_numeric(temp_f)
        kelvin = (temp_f + 459.67) * 5 / 9
        return round(kelvin, 4)
    def celsius_to_fahrenheit(self, temp_c):
        self._validate_numeric(temp_c)
        fahrenheit = temp_c * 9 / 5 + 32
        return round(fahrenheit, 4)
    def celsius_to_kelvin(self, temp_c):
        self._validate_numeric(temp_c)
        kelvin = temp_c + 273.15
        return round(kelvin, 4)
    def kelvin_to_fahrenheit(self, temp_k):
        self._validate_numeric(temp_k)
        fahrenheit = (temp_k - 273.15) * 9 / 5 + 32
        return round(fahrenheit, 4)
    def kelvin_to_celsius(self, temp_k):
        self._validate_numeric(temp_k)
        celsius = temp_k - 273.15
        return round(celsius, 4)
    def fahrenheit_to_rankine(self, temp_f):
        self._validate_numeric(temp_f)
        rankine = temp_f + 459.67
        return round(rankine, 4)
    def celsius_to_rankine(self, temp_c):
        self._validate_numeric(temp_c)
        kelvin = temp_c + 273.15
        rankine = kelvin * 9 / 5
        return round(rankine, 4)
if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_fahrenheit_values = [0, 32, 100]
    sample_celsius_values = [-40, 0, 100]
    sample_kelvin_values = [0, 273.15, 373.15]
    print("Fahrenheit to Celsius:")
    for val in sample_fahrenheit_values:
        result = converter.fahrenheit_to_celsius(val)
        print(f"{val}°F -> {result}°C")
    print("\nFahrenheit to Kelvin:")
    for val in sample_fahrenheit_values:
        result = converter.fahrenheit_to_kelvin(val)
        print(f"{val}°F -> {result}K")
    print("\nCelsius to Fahrenheit:")
    for val in sample_celsius_values:
        result = converter.celsius_to_fahrenheit(val)
        print(f"{val}°C -> {result}°F")
    print("\nCelsius to Kelvin:")
    for val in sample_celsius_values:
        result = converter.celsius_to_kelvin(val)
        print(f"{val}°C -> {result}K")
    print("\nKelvin to Fahrenheit:")
    for val in sample_kelvin_values:
        result = converter.kelvin_to_fahrenheit(val)
        print(f"{val}K -> {result}°F")
    print("\nKelvin to Celsius:")
    for val in sample_kelvin_values:
        result = converter.kelvin_to_celsius(val)
        print(f"{val}K -> {result}°C")
    print("\nFahrenheit to Rankine:")
    for val in sample_fahrenheit_values:
        result = converter.fahrenheit_to_rankine(val)
        print(f"{val}°F -> {result}°R")
    print("\nCelsius to Rankine:")
    for val in sample_celsius_values:
        result = converter.celsius_to_rankine(val)
        print(f"{val}°C -> {result}°R")