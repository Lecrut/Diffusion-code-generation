class SumCalculator:
    @staticmethod
    def add_values(a, b):
        return a + b

if __name__ == '__main__':
    calc = SumCalculator()
    print(calc.add_values(3, 5))
    print(calc.add_values(-1, 4))