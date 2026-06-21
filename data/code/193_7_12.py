class SumCalculator:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def calculate_total(self):
        return sum(self.numbers)

if __name__ == '__main__':
    calculator = SumCalculator([10, 25, 30, 45, 50])
    total_sum = calculator.calculate_total()
    print(total_sum)