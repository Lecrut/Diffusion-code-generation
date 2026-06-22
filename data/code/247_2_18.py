class SumCalculator:
    def calculate_sum(self, a, b):
        return a + b

if __name__ == '__main__':
    calculator = SumCalculator()
    print(f"10 + 5 = {calculator.calculate_sum(10, 5)}")
    print(f"7 + 3 = {calculator.calculate_sum(7, 3)}")