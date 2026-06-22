class SumCalculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def calculate_sum(self):
        return self.num1 + self.num2

if __name__ == '__main__':
    calculator = SumCalculator(5, 7)
    result = calculator.calculate_sum()
    print(result)