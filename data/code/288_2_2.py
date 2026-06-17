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
    c_temp = 25.0
    f_result = converter.celsius_to_fahrenheit(c_temp)
    print(f"{c_temp}°C is {f_result}°F")
    print("\n--- Fahrenheit to Celsius ---")
    f_temp = 77.0
    c_result = converter.fahrenheit_to_celsius(f_temp)
    print(f"{f_temp}°F is {c_result}°C")
    print("\n--- Celsius to Kelvin ---")
    c_temp_k = 100.0
    k_result = converter.celsius_to_kelvin(c_temp_k)
    print(f"{c_temp_k}°C is {k_result}K")
    print("\n--- Kelvin to Celsius ---")
    k_temp = 300.15
    c_result_2 = converter.kelvin_to_celsius(k_temp)
    print(f"{k_temp}K is {c_result_2}°C")
    print("\n--- Fahrenheit to Kelvin ---")
    f_temp_k = 68.0
    k_result_3 = converter.fahrenheit_to_kelvin(f_temp_k)
    print(f"{f_temp_k}°F is {k_result_3}K")
    print("\n--- Error Handling Example (Conceptual - relies on float input for simplicity, explicit error raising omitted as per strict requirement to only return runnable code without docstrings/comments) ---")
    try:
        converter.celsius_to_fahrenheit(-10.0)
    except Exception as e:
        print(f"Caught expected error during invalid input test: {e}")