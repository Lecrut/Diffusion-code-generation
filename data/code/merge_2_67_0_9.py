class TemperatureConverter:
    def to_fahrenheit(self, celsius):
        if not isinstance(celsius, (int, float)):
            raise TypeError("Input must be a number.")
        return (celsius * 9 / 5) + 32
    def to_kelvin(self, celsius):
        if not isinstance(celsius, (int, float)):
            raise TypeError("Input must be a number.")
        return celsius + 273.15
def main():
    converter = TemperatureConverter()
    try:
        sample_celsius = -40
        fahrenheit_result = converter.to_fahrenheit(sample_celsius)
        kelvin_result = converter.to_kelvin(sample_celsius)
        print(f"{sample_celsius}°C is {fahrenheit_result:.2f}°F")
        print(f"{sample_celsius}°C is {kelvin_result:.2f}K")
    except (TypeError, ValueError) as e:
        print(f"Error during conversion: {e}")
if __name__ == '__main__':
    main()