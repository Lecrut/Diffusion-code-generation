class TemperatureComparator:
    def __init__(self, temp1, temp2):
        self.temp1 = self.validate_temperature(temp1)
        self.temp2 = self.validate_temperature(temp2)

    @staticmethod
    def validate_temperature(temp):
        if not isinstance(temp, (int, float)):
            raise ValueError("Temperature must be a number.")
        return temp

    def compare(self):
        if self.temp1 > self.temp2:
            return "Temperature 1 is higher than Temperature 2"
        elif self.temp1 < self.temp2:
            return "Temperature 1 is lower than Temperature 2"
        else:
            return "Both temperatures are equal"

    def absolute_difference(self):
        return abs(self.temp1 - self.temp2)

if __name__ == '__main__':
    comparator = TemperatureComparator(40, 35)
    print(comparator.compare())
    print("Absolute Difference:", comparator.absolute_difference())