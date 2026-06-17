class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        if not isinstance(celsius, (int, float)):
            raise TypeError("Input must be a number.")
        return (celsius * 9 / 5) + 32
    def fahrenheit_to_celsius(self, fahrenheit):
        if not isinstance(fahrenheit, (int, float)):
            raise TypeError("Input must be a number.")
        return (fahrenheit - 32) * 5 / 9
    def celsius_to_kelvin(self, celsius):
        if not isinstance(celsius, (int, float)):
            raise TypeError("Input must be a number.")
        return celsius + 273.15
    def kelvin_to_celsius(self, kelvin):
        if not isinstance(kelvin, (int, float)):
            raise TypeError("Input must be a number.")
        return kelvin - 273.15
    def fahrenheit_to_kelvin(self, fahrenheit):
        if not isinstance(fahrenheit, (int, float)):
            raise TypeError("Input must be a number.")
        celsius = self.fahrenheit_to_celsius(fahrenheit)
        return celsius + 273.15
if __name__ == '__main__':
    converter = TemperatureConverter()
    try:
        result_cf = converter.celsius_to_fahrenheit(0)
        print(f"0°C is {result_cf}°F")
        result_ck = converter.celsius_to_kelvin(100)
        print("100°C is", result_ck, "K")
        result_fc = converter.fahrenheit_to_celsius(212)
        print("212°F is", result_fc, "°C")
        result_fk = converter.fahrenheit_to_kelvin(32)
        print("32°F is", result_fk, "K")
        result_ka = converter.kelvin_to_celsius(0)
        print("0 K is", result_ka, "°C")
    except (TypeError, ValueError) as e:
        print(f"Error occurred during conversion: {e}")