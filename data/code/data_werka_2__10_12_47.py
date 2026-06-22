class TemperatureAnalyzer:

    def __init__(self, temp1, temp2):
        self.temp1 = float(temp1)
        self.temp2 = float(temp2)
        self.tolerance = 1e-09

    def are_close(self):
        return abs(self.temp1 - self.temp2) < self.tolerance

    def compare(self):
        if self.are_close():
            return 'equal'
        elif self.temp1 < self.temp2:
            return 'less than'
        else:
            return 'greater than'
if __name__ == '__main__':
    temp_value1 = 40.6000000005
    temp_value2 = 40.6
    analyzer = TemperatureAnalyzer(temp_value1, temp_value2)
    relationship = analyzer.compare()
    print(relationship)
    is_close_result = analyzer.are_close()
    print(is_close_result)