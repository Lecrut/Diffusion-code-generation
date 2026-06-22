class SumCalculator:
    def sum_values(self):
        return -10 + (-5) + 0 + 5 + 10 + 15

if __name__ == '__main__':
    calculator = SumCalculator()
    result1 = calculator.sum_values()
    print(f"Sum of (-10, -5, 0, 5, 10, 15): {result1}")