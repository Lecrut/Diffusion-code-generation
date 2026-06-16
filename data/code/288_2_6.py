class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius: float) -> float:
        return (celsius * 9/5) + 32
    def fahrenheit_to_celsius(self, fahrenheit: float) -> float:
        return (fahrenheit - 32) * 5/9
    def celsius_to_kelvin(self, celsius: float) -> float:
        return celsius + 273.15
    def kelvin_to_celsius(self, kelvin: float) -> float:
        return kelvin - 273.15
    def fahrenheit_to_kelvin(self, fahrenheit: float) -> float:
        celsius = self.fahrenheit_to_celsius(fahrenheit)
        return self.celsius_to_kelvin(celsius)
    def kelvin_to_fahrenheit(self, kelvin: float) -> float:
        celsius = self.kelvin_to_celsius(kelvin)
        return self.celsius_to_fahrenheit(celsius)
if __name__ == '__main__':
    converter = TemperatureConverter()
    print("--- Celsius to Fahrenheit ---")
    celsius_val = 25.0
    fahrenheit_result = converter.celsius_to_fahrenheit(celsius_val)
    print(f"{celsius_val}°C is {fahrenheit_result}°F")
    print("\n--- Fahrenheit to Celsius ---")
    fahrenheit_val = 77.0
    celsius_result = converter.fahrenheit_to_celsius(fahrenheit_val)
    print(f"{fahrenheit_val}°F is {celsius_result}°C")
    print("\n--- Celsius to Kelvin ---")
    celsius_val = 100.0
    kelvin_result = converter.celsius_to_kelvin(celsius_val)
    print(f"{celsius_val}°C is {kelvin_result}K")
    print("\n--- Kelvin to Celsius ---")
    kelvin_val = 300.15
    celsius_result = converter.kelvin_to_celsius(kelvin_val)
    print(f"{kelvin_val}K is {celsius_result}°C")
    print("\n--- Fahrenheit to Kelvin ---")
    fahrenheit_val = 68.0
    kelvin_result = converter.fahrenheit_to_kelvin(fahrenheit_val)
    print(f"{fahrenheit_val}°F is {kelvin_result}K")
    print("\n--- Kelvin to Fahrenheit ---")
    kelvin_val = 300.15
    fahrenheit_result = converter.kelvin_to_fahrenheit(kelvin_val)
    print(f"{kelvin_val}K is {fahrenheit_result}°F")
    print("\n--- Error Handling Example (Conceptual - Python type hints handle basic safety, explicit error raising would be added for stricter runtime validation if needed) ---")
    try:
        converter.celsius_to_fahrenheit(-10.0)
    except Exception as e:
        print(f"Caught an error during invalid input test: {e}")