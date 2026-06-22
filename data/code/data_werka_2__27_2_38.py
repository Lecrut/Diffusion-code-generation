class ValueChecker:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def are_values_different(self):
        return self.a != self.b

if __name__ == '__main__':
    checker = ValueChecker(5, 10)
    print(checker.are_values_different())