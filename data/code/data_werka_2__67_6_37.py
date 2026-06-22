class SumCalculator:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def compute_sum(self):
        return self.attribute1 + self.attribute2

if __name__ == '__main__':
    FIRST_ATTRIBUTE = 4
    SECOND_ATTRIBUTE = 9
    calculator = SumCalculator(FIRST_ATTRIBUTE, SECOND_ATTRIBUTE)
    result = calculator.compute_sum()
    print(result)