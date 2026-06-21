class TemperatureComparator:
    def __init__(self, temp1, temp2):
        self.temp1 = temp1
        self.temp2 = temp2

    def compare(self):
        if self.temp1 > self.temp2:
            return "Temperature 1 is higher than Temperature 2"
        if self.temp1 < self.temp2:
            return "Temperature 1 is lower than Temperature 2"
        return "Both temperatures are equal"

    def absolute_difference(self):
        return abs(self.temp1 - self.temp2)

if __name__ == '__main__':
    comparator = TemperatureComparator(35, 40)
    print(comparator.compare())
    print("Absolute Difference:", comparator.absolute_difference())