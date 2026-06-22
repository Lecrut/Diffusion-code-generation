class TemperatureCalculator:
    def average_celsius_to_fahrenheit(self, temperatures: list) -> float:
        if not temperatures:
            return 0.0
        avg_celsius = sum(temperatures) / len(temperatures)
        return (avg_celsius * 9/5) + 32

if __name__ == '__main__':
    calculator = TemperatureCalculator()
    sample_temps = [10, 20, 30, 40]
    print(f"Average temperature in Fahrenheit: {calculator.average_celsius_to_fahrenheit(sample_temps)}")