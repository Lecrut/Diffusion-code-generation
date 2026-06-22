class SumCalculator:
    def sum(self, a, b):
        return a + b

if __name__ == '__main__':
    calc = SumCalculator()
    result1 = calc.sum(3, 5)
    print(result1)
    result2 = calc.sum(7, 9)
    print(result2)