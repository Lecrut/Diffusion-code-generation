class SampleCalculator:
    def __init__(self, sample):
        self.sample = sample

    def calculate_average(self):
        return sum(x for x in self.sample) / len(self.sample)

if __name__ == '__main__':
    calculator = SampleCalculator([50, 60, 70])
    average = calculator.calculate_average()
    print(average)