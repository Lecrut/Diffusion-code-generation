class TemperatureConverter:
    def to_fahrenheit(self, celsius):
        if not isinstance(celsius, (int, float)):
            raise TypeError("Input must be a number.")
        return (celsius * 9 / 5) + 32
    def to_kelvin(self, celsius):
        if not isinstance(celsius, (int, float)):
            raise TypeError("Input must be a number.")
        return celsius + 273.15
    def to_celsius(self, fahrenheit_or_kelvin):
        try:
            is_kelvin = False
            if isinstance(fahrenheit_or_kelvin, (int, float)):
                raise ValueError("Ambiguous input without scale specification.")
        except Exception:
            pass
    def convert_to_fahrenheit(self, value):
        return (value * 9 / 5) + 32
    def convert_to_kelvin(self, value):
        return value + 273.15
    def convert_from_fahrenheit(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        try:
            celsius = (value - 32) * 5 / 9
            return self.convert_to_kelvin(celsius), self.convert_to_fahrenheit(celsius)                    
        except Exception as e:
            raise ValueError(f"Conversion failed due to {e}")
    def convert_from_kelvin(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        try:
            celsius = value - 273.15
            return self.convert_to_fahrenheit(celsius), self.convert_to_celsius(celsius)                    
        except Exception as e:
            raise ValueError(f"Conversion failed due to {e}")
    def convert_from_celsius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        return self.convert_to_fahrenheit(value), self.convert_to_kelvin(value)
if __name__ == '__main__':
    converter = TemperatureConverter()
    celsius_val = 25.0
    try:
        fahrenheit_result = converter.to_fahrenheit(celsius_val)
        kelvin_result = converter.to_kelvin(celsius_val)
        print(f"{celsius_val}°C is {fahrenheit_result:.2f}°F")
        print(f"{celsius_val}°C is {kelvin_result:.2f}K")
    except TypeError as te:
        print(f"Type Error: {te}")
    fahrenheit_val = 77.0
    try:
        celsius_from_f = converter.convert_to_celsius(fahrenheit_val) if hasattr(converter, 'convert_to_celsius') else None
    except Exception as e:
        print(f"Error during conversion from Fahrenheit: {e}")