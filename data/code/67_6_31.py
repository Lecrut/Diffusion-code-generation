class SumCalculator:

    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def compute_sum(self):
        return self.attribute1 + self.attribute2
if __name__ == '__main__':
    value1 = 4
    value2 = 9
    calculator_instance = SumCalculator(value1, value2)
    result = calculator_instance.compute_sum()
    print('The sum is:', result)
    another_value1 = 12
    another_value2 = 23
    another_calculator_instance = SumCalculator(another_value1, another_value2)
    another_result = another_calculator_instance.compute_sum()
    print('Another sum is:', another_result)