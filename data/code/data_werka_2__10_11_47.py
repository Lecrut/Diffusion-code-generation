class TemperatureCalculator:
    def __init__(self, temp1, temp2):
        self.temp1 = temp1
        self.temp2 = temp2

    def calculate_difference(self):
        return abs(self.temp1 - self.temp2)

if __name__ == '__main__':
    sample_temp1 = 35.6
    sample_temp2 = 40.2
    calculator = TemperatureCalculator(sample_temp1, sample_temp2)
    result = calculator.calculate_difference()
    print(result)