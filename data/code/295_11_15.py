class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius: float) -> float:
        return (celsius * 9/5) + 32

    def fahrenheit_to_celsius(self, fahrenheit: float) -> float:
        return (fahrenheit - 32) * 5/9

if __name__ == '__main__':
    converter = TemperatureConverter()
    temp_c = 0
    temp_f = converter.celsius_to_fahrenheit(temp_c)
    print(f"{temp_c}°C is {temp_f:.1f}°F")
    
    temp_f = 32
    temp_c = converter.fahrenheit_to_celsius(temp_f)
    print(f"{temp_f}°F is {temp_c:.1f}°C")