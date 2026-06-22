def compute_sum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Both inputs must be either integers or floating-point numbers.')
    return a + b

class SumCalculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        return compute_sum(self.a, self.b)
if __name__ == '__main__':
    calculator1 = SumCalculator(5, 3)
    print(calculator1.calculate())
    calculator2 = SumCalculator(2.5, 4.7)
    print(calculator2.calculate())
    calculator3 = SumCalculator(-1, -1)
    print(calculator3.calculate())
    calculator4 = SumCalculator(0, 0)
    print(calculator4.calculate())
    calculator5 = SumCalculator(100, 200.5)
    print(calculator5.calculate())