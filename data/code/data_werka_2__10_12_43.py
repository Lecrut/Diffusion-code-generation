import math

class TemperatureAnalyzer:
    def __init__(self, temp1, temp2):
        self.temp1 = temp1
        self.temp2 = temp2
        self.tolerance = 1e-09

    def are_equal(self):
        return math.isclose(self.temp1, self.temp2, abs_tol=self.tolerance)

    def compare(self):
        if self.are_equal():
            return 'equal'
        elif self.temp1 < self.temp2:
            return 'less than'
        else:
            return 'greater than'

if __name__ == '__main__':
    temperature1 = 40.6000000005
    temperature2 = 40.6
    analyzer = TemperatureAnalyzer(temperature1, temperature2)
    
    print(analyzer.compare())
    print(analyzer.are_equal())