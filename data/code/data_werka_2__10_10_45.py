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

    @staticmethod
    def absolute_difference(temp1, temp2):
        return abs(temp1 - temp2)

if __name__ == '__main__':
    comparator = TemperatureComparator(35, 40)
    print(comparator.compare())
    difference = TemperatureComparator.absolute_difference(35, 40)
    print("Absolute Difference:", difference)