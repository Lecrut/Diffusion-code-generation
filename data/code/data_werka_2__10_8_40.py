class TemperatureAnalyzer:
    def __init__(self, temperatures):
        if len(temperatures) != 2 or not all(isinstance(temp, (int, float)) for temp in temperatures):
            raise ValueError("Exactly two numeric temperature readings are required.")
        self.temperatures = temperatures

    def calculate_mean(self):
        return round(sum(self.temperatures) / len(self.temperatures), 2)

if __name__ == '__main__':
    sample_temps = [30.5, 25.8]
    analyzer = TemperatureAnalyzer(sample_temps)
    mean_temperature = analyzer.calculate_mean()
    print(mean_temperature)