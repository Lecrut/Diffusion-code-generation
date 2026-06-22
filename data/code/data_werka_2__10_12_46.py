class TemperatureAnalyzer:
    def __init__(self, temp1, temp2):
        self.temp1 = float(temp1)
        self.temp2 = float(temp2)
        self.tolerance = 1e-09

    def _are_close(self):
        return abs(self.temp1 - self.temp2) < self.tolerance

    def compare(self):
        if self._are_close():
            return 'equal'
        elif self.temp1 < self.temp2:
            return 'less than'
        else:
            return 'greater than'

if __name__ == '__main__':
    temperature1 = 40.6000000005
    temperature2 = 40.6
    analyzer = TemperatureAnalyzer(temperature1, temperature2)
    relationship = analyzer.compare()
    print(relationship)