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
    celsius_temp = 25.0
    fahrenheit_result = converter.celsius_to_fahrenheit(celsius_temp)
    print(f"{celsius_temp}°C is {fahrenheit_result}°F")
    print("\n--- Fahrenheit to Celsius ---")
    fahrenheit_temp = 77.0
    celsius_result = converter.fahrenheit_to_celsius(fahrenheit_temp)
    print(f"{fahrenheit_temp}°F is {celsius_result}°C")
    print("\n--- Celsius to Kelvin ---")
    celsius_temp_k = 100.0
    kelvin_result = converter.celsius_to_kelvin(celsius_temp_k)
    print(f"{celsius_temp_k}°C is {kelvin_result}K")
    print("\n--- Kelvin to Celsius ---")
    kelvin_temp = 300.15
    celsius_result_2 = converter.kelvin_to_celsius(kelvin_temp)
    print(f"{kelvin_temp}K is {celsius_result_2}°C")
    print("\n--- Fahrenheit to Kelvin ---")
    fahrenheit_temp_k = 68.0
    kelvin_result_3 = converter.fahrenheit_to_kelvin(fahrenheit_temp_k)
    print(f"{fahrenheit_temp_k}°F is {kelvin_result_3}K")
    print("\n--- Kelvin to Fahrenheit ---")
    kelvin_temp_2 = 300.15
    fahrenheit_result_4 = converter.kelvin_to_fahrenheit(kelvin_temp_2)
    print(f"{kelvin_temp_2}K is {fahrenheit_result_4}°F")
    print("\n--- Error Handling Example (Implicit Type Safety via float operations) ---")
    try:
        converter.celsius_to_fahrenheit("invalid")
    except TypeError as e:
        print(f"Caught expected error for invalid input type: {e}")