class SumCalculator:
    def sum_two_integers(self, a: int, b: int) -> int:
        return a + b

if __name__ == '__main__':
    calculator = SumCalculator()
    result1 = calculator.sum_two_integers(3, 5)
    result2 = calculator.sum_two_integers(7, 9)
    print(result1)
    print(result2)