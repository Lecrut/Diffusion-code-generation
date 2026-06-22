class SumCalculator:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
    
    def calculate_sum(self):
        return self.value1 + self.value2

if __name__ == '__main__':
    calculator = SumCalculator(4, 6)
    result = calculator.calculate_sum()
    print(result)