from functools import reduce
import operator

class SumCalculator:
    def __init__(self, data):
        self.data = data
    
    def calculate_sum(self):
        return reduce(operator.add, self.data)

if __name__ == '__main__':
    calculator = SumCalculator([12345678901234567890, 98765432109876543210, 11111111111111111111])
    result = calculator.calculate_sum()
    print(result)