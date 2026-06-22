class TemperatureComparator:
    def __init__(self, temp1, temp2):
        self.temp1 = temp1
        self.temp2 = temp2
        self.epsilon = 1e-09

    def compare(self):
        if abs(self.temp1 - self.temp2) < self.epsilon:
            return 'equal'
        elif self.temp1 < self.temp2:
            return 'less than'
        else:
            return 'greater than'

if __name__ == '__main__':
    temperature1 = 37.5000000002
    temperature2 = 37.5
    comparator = TemperatureComparator(temperature1, temperature2)
    relationship = comparator.compare()
    print(relationship)