class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

if __name__ == '__main__':
    converter = TemperatureConverter()
    fahrenheit_result = converter.celsius_to_fahrenheit(0)
    print(f"0°C is {fahrenheit_result}°F")
    
    fahrenheit_result_2 = converter.celsius_to_fahrenheit(100)
    print(f"100°C is {fahrenheit_result_2}°F")