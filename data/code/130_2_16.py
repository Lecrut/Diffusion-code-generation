class ZeroChecker:
    def __init__(self):
        self.zero_values = {0: True, 0.0: True}

    def is_zero(self, value):
        return value in self.zero_values

if __name__ == '__main__':
    checker = ZeroChecker()
    print(checker.is_zero(0))
    print(checker.is_zero(0.0))
    print(checker.is_zero(-0))
    print(checker.is_zero(-0.0))
    print(checker.is_zero(1))
    print(checker.is_zero(1.0))