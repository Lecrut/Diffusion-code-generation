class IntegerChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_positivity(self):
        return self.a > 0

    def check_evenness(self):
        return self.b % 2 == 0

    def check_divisibility(self):
        if self.a == 0:
            return False
        return self.c % self.a == 0

    def run_all_checks(self):
        return (
            self.check_positivity(),
            self.check_evenness(),
            self.check_divisibility()
        )

if __name__ == '__main__':
    checker = IntegerChecker(7, 8, 21)
    print(checker.run_all_checks())
    print(checker.check_positivity())
    print(checker.check_evenness())
    print(checker.check_divisibility())