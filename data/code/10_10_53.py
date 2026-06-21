class TemperatureComparator:
    def __init__(self, temp1, temp2):
        self.temp1 = temp1
        self.temp2 = temp2

    def compare(self):
        if self.temp1 > self.temp2:
            return f"{self.temp1} is higher than {self.temp2}"
        elif self.temp1 < self.temp2:
            return f"{self.temp1} is lower than {self.temp2}"
        else:
            return f"{self.temp1} is equal to {self.temp2}"

    def absolute_difference(self):
        return abs(self.temp1 - self.temp2)

if __name__ == '__main__':
    comparator = TemperatureComparator(30, 25)
    print(comparator.compare())
    print("Absolute Difference:", comparator.absolute_difference())