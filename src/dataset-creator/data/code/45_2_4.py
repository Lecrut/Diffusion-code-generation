class Calculator:
    def total(self, a, b):
        return a + b
if __name__ == '__main__':
    calc = Calculator()
    sample_a = 10
    sample_b = 25
    result = calc.total(sample_a, sample_b)
    print(result)