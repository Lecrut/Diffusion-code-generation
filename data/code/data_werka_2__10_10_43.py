class TemperatureComparator:
    def __init__(self, temp1, temp2):
        self.temp1 = temp1
        self.temp2 = temp2

    def compare(self):
        if self.temp1 > self.temp2:
            return "Temperature 1 is higher than Temperature 2"
        elif self.temp1 < self.temp2:
            return "Temperature 1 is lower than Temperature 2"
        else:
            return "Both temperatures are equal"

    def absolute_difference(self):
        difference = abs(self.temp1 - self.temp2)
        return difference

if __name__ == '__main__':
    comparator = TemperatureComparator(20, 15)
    comparison_result = comparator.compare()
    print(comparison_result)
    difference = comparator.absolute_difference()
    print("Absolute Difference:", difference)