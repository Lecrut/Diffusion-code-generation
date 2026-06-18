class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        if not isinstance(celsius, (int, float)):
            raise TypeError("Temperature must be a number.")
        return (celsius * 9/5) + 32
    def fahrenheit_to_celsius(self, fahrenheit):
        if not isinstance(fahrenheit, (int, float)):
            raise TypeError("Temperature must be a number.")
        return (fahrenheit - 32) * 5/9
    def celsius_to_kelvin(self, celsius):
        if not isinstance(celsius, (int, float)):
            raise TypeError("Temperature must be a number.")
        return celsius + 273.15
    def kelvin_to_celsius(self, kelvin):
        if not isinstance(kelvin, (int, float)):
            raise TypeError("Temperature must be a number.")
        return kelvin - 273.15
if __name__ == '__main__':
    converter = TemperatureConverter()
    celsius_sample = 0
    fahrenheit_result = converter.celsius_to_fahrenheit(celsius_sample)
    print(f"{celsius_sample}°C is {fahrenheit_result:.2f}°F")
    kelvin_sample = 373.15
    celsius_from_kelvin = converter.kelvin_to_celsius(kelvin_sample)
    print(f"{kelvin_sample}K is {celsius_from_kelvin:.2f}°C")
    fahrenheit_sample = 212
    celsius_result = converter.fahrenheit_to_celsius(fahrenheit_sample)
    print(f"{fahrenheit_sample}°F is {celsius_result:.2f}°C")
    kelvin_error_test = "invalid"
    try:
        result = converter.celsius_to_kelvin(kelvin_error_test)
    except TypeError as e:
        print(f"Error caught for invalid input: {e}")