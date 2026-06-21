class SumCalculator:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def compute_sum(self):
        return self.attribute1 + self.attribute2

if __name__ == '__main__':
    first_attribute = 20
    second_attribute = 30
    calculator = SumCalculator(first_attribute, second_attribute)
    total_sum = calculator.compute_sum()
    print(total_sum)