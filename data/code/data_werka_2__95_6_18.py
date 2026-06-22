class TripleAttributeAnalyzer:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_positive(self):
        return self.a > 0

    def check_even(self):
        return self.b % 2 == 0

    def check_divisibility(self):
        if self.a == 0:
            return False
        return self.c % self.a == 0

    def run_all_checks(self):
        return self.check_positive() and self.check_even() and self.check_divisibility()

if __name__ == '__main__':
    analyzer = TripleAttributeAnalyzer(4, 10, 20)
    print(analyzer.check_positive())
    print(analyzer.check_even())
    print(analyzer.check_divisibility())
    print(analyzer.run_all_checks())