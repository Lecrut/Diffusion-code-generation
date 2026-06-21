class TemperatureComparison:

    def __init__(self, temp1, temp2):
        self.temp1 = float(temp1)
        self.temp2 = float(temp2)
        self.precision_threshold = 1e-09

    def is_close(self):
        return abs(self.temp1 - self.temp2) < self.precision_threshold

    def compare(self):
        if self.is_close():
            return 'equal'
        elif self.temp1 < self.temp2:
            return 'less than'
        else:
            return 'greater than'
if __name__ == '__main__':
    temperature1 = 39.5000000004
    temperature2 = 39.5
    comparator = TemperatureComparison(temperature1, temperature2)
    relationship = comparator.compare()
    print(relationship)
    close_check = comparator.is_close()
    print(close_check)