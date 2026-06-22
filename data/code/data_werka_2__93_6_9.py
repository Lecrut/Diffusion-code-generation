class FalseChecker:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def is_both_false(self):
        return not bool(self.a) and not bool(self.b)

    def get_truth_values(self):
        return not bool(self.a), not bool(self.b)

if __name__ == '__main__':
    checker = FalseChecker(0, [])
    print(checker.is_both_false())
    print(checker.get_truth_values())