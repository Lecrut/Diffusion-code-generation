class DiscountCalculator:
    def __init__(self, rates):
        self.rates = rates

    def apply(self, value, rate_index):
        return value * (1.0 - self.rates[rate_index])

    def compute_all(self, values):
        return [self.apply(v, 0) for v in values]

if __name__ == '__main__':
    calc = DiscountCalculator([0.05])
    hard_values = [100, 200, 300]
    computed = calc.compute_all(hard_values)
    print(computed)
    print(calc.apply(150, 0))