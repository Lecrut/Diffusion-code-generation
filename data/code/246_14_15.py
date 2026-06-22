class SumCalculator:
    def add(self, a: int, b: int) -> int:
        return a + b

if __name__ == '__main__':
    calc = SumCalculator()
    result1 = calc.add(5, 3)
    result2 = calc.add(10, 7)
    print(result1)
    print(result2)