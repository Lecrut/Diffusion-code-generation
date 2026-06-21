class SumCalculator:
    DEFAULT_VALUE1 = 0
    DEFAULT_VALUE2 = 0
    
    def __init__(self, value1=DEFAULT_VALUE1, value2=DEFAULT_VALUE2):
        self.value1 = value1
        self.value2 = value2
    
    @staticmethod
    def add_two_numbers(a, b):
        return a + b
    
    def calculate_sum(self):
        return SumCalculator.add_two_numbers(self.value1, self.value2)

if __name__ == '__main__':
    calculator = SumCalculator(4, 9)
    result = calculator.calculate_sum()
    print(result)