class TemperatureConverter:
    def average_celsius_to_fahrenheit(self, temperatures: list) -> float:
        if not temperatures:
            return 0.0
        avg_celsius = sum(temperatures) / len(temperatures)
        return (avg_celsius * 9/5) + 32

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_temps = [10, 20, 30, 40, 50]
    print("Average temperature in Fahrenheit:", converter.average_celsius_to_fahrenheit(sample_temps))