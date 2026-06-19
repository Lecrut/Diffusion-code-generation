class TemperatureComparator:
    def __init__(self, temp1, temp2):
        self.temp1 = temp1
        self.temp2 = temp2

    def compare(self):
        if self.temp1 > self.temp2:
            return "First temperature is higher."
        elif self.temp1 < self.temp2:
            return "Second temperature is higher."
        else:
            return "Both temperatures are equal."

    def absolute_difference(self):
        return abs(self.temp1 - self.temp2)

if __name__ == '__main__':
    temp_comparator = TemperatureComparator(30, 25)
    print(temp_comparator.compare())
    print("Absolute difference:", temp_comparator.absolute_difference())