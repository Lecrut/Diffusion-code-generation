class TemperatureComparator:
    WARMER_BY_TEMPLATE = "{} is warmer by {} degrees"
    EQUAL_TEMPERATURES = "Both temperatures are equal"

    @staticmethod
    def validate_temperature(temp):
        if not isinstance(temp, (int, float)):
            raise ValueError("Temperature must be a number")

    def __init__(self, temp1, temp2):
        self.validate_temperature(temp1)
        self.validate_temperature(temp2)
        self.temp1 = temp1
        self.temp2 = temp2

    def compare(self):
        difference = abs(self.temp1 - self.temp2)
        if self.temp1 > self.temp2:
            yield self.WARMER_BY_TEMPLATE.format("T1", difference)
        elif self.temp2 > self.temp1:
            yield self.WARMER_BY_TEMPLATE.format("T2", difference)
        else:
            yield self.EQUAL_TEMPERATURES

if __name__ == '__main__':
    comparator = TemperatureComparator(30, 25)
    for result in comparator.compare():
        print(result)

    comparator = TemperatureComparator(28, 35)
    for result in comparator.compare():
        print(result)

    comparator = TemperatureComparator(20, 20)
    for result in comparator.compare():
        print(result)

    comparator = TemperatureComparator(15, 22)
    for result in comparator.compare():
        print(result)