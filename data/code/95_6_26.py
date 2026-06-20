class AttributeChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_positive(self):
        return self.a > 0

    def check_even(self):
        return self.b % 2 == 0

    def check_divisible(self):
        return self.c % self.a == 0

if __name__ == '__main__':
    checker = AttributeChecker(5, 4, 10)
    print(checker.check_positive())
    print(checker.check_even())
    print(checker.check_divisible())