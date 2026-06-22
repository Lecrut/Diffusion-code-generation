class TemperatureComparator:
    def __init__(self, temp1, temp2):
        self.temp1 = temp1
        self.temp2 = temp2

    def compare_temperatures(self):
        if self.temp1 > self.temp2:
            return f"{self.temp1} is higher than {self.temp2}"
        elif self.temp1 < self.temp2:
            return f"{self.temp1} is lower than {self.temp2}"
        else:
            return f"{self.temp1} is equal to {self.temp2}"

    def calculate_difference(self):
        return abs(self.temp1 - self.temp2)

if __name__ == '__main__':
    temp_comparator = TemperatureComparator(30, 25)
    print(temp_comparator.compare_temperatures())
    print(f"The absolute difference is: {temp_comparator.calculate_difference()}")