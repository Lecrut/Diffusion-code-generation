class TemperatureAnalyzer:

    def __init__(self):
        self.temperatures = []

    def add_temperature(self, temperature):
        if not isinstance(temperature, (int, float)):
            raise ValueError('Temperature must be a number')
        self.temperatures.append(temperature)

    def calculate_range(self):
        if not self.temperatures:
            return 0
        minimum = min(self.temperatures)
        maximum = max(self.temperatures)
        return maximum - minimum
if __name__ == '__main__':
    analyzer = TemperatureAnalyzer()
    analyzer.add_temperature(10)
    analyzer.add_temperature(5)
    analyzer.add_temperature(20)
    result1 = analyzer.calculate_range()
    print(result1)
    analyzer.add_temperature(-5)
    analyzer.add_temperature(100)
    result2 = analyzer.calculate_range()
    print(result2)