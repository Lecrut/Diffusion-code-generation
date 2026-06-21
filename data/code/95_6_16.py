class MultiAttributeAnalyzer:
    VALIDATION_RULES = {
        'a_positive': lambda obj: obj.a > 0,
        'b_even': lambda obj: obj.b % 2 == 0,
        'c_div_a': lambda obj: obj.c % obj.a == 0 if obj.a != 0 else False,
    }

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def analyze(self):
        checks = self.VALIDATION_RULES
        results = [
            checks['a_positive'](self),
            checks['b_even'](self),
            checks['c_div_a'](self),
        ]
        return all(results)

if __name__ == '__main__':
    analyzer = MultiAttributeAnalyzer(3, 6, 9)
    outcome = analyzer.analyze()
    print(outcome)