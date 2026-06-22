class SumCalculator:
    def calculate_sum(self, x, y):
        return x + y

if __name__ == '__main__':
    calculator = SumCalculator()
    print(f"10 + 5 = {calculator.calculate_sum(10, 5)}")
    print(f"3.14 + 2 = {calculator.calculate_sum(3.14, 2)}")