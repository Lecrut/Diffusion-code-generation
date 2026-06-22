class SumCalculator:

    def __init__(self, value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b

    def get_sum(self):
        return self.value_a + self.value_b
if __name__ == '__main__':
    sum_calculator = SumCalculator(10, 20)
    result1 = sum_calculator.get_sum()
    print(result1)
    another_calculator = SumCalculator(5, 15)
    result2 = another_calculator.get_sum()
    print(result2)