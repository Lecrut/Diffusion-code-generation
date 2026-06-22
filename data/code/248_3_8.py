class SumCalculator:
    def add(self, a, b):
        return a + b

if __name__ == '__main__':
    calc = SumCalculator()
    result1 = calc.add(3, 5)
    print(result1)
    result2 = calc.add(7, 9)
    print(result2)