class TemperatureAnalyzer:
    DEFAULT_PRECISION = 1e-09

    def __init__(self, temp1, temp2):
        self.temp1 = float(temp1)
        self.temp2 = float(temp2)
        self.precision_threshold = TemperatureAnalyzer.DEFAULT_PRECISION

    def are_temperatures_equal(self):
        return abs(self.temp1 - self.temp2) < self.precision_threshold

    def compare_temperatures(self):
        if self.are_temperatures_equal():
            return 'equal'
        elif self.temp1 < self.temp2:
            return 'less than'
        else:
            return 'greater than'

if __name__ == '__main__':
    temperature1 = 40.6000000005
    temperature2 = 40.6

    analyzer = TemperatureAnalyzer(temperature1, temperature2)
    
    print(analyzer.compare_temperatures())
    print(analyzer.are_temperatures_equal())