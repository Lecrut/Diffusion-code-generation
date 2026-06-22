class NumberAnalyzer:
    def __init__(self, value):
        self.value = value

    def is_positive(self):
        return self.value > 0

    def is_even(self):
        return self.value % 2 == 0

    def is_divisible_by_three(self):
        return self.value % 3 == 0

    def get_checks(self):
        return {
            "positive": self.is_positive(),
            "even": self.is_even(),
            "divisible_by_three": self.is_divisible_by_three()
        }

if __name__ == '__main__':
    analyzer = NumberAnalyzer(12)
    print(analyzer.get_checks())
    analyzer2 = NumberAnalyzer(-3)
    print(analyzer2.get_checks())
    analyzer3 = NumberAnalyzer(7)
    print(analyzer3.get_checks())