class AttributeChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self):
        return self.a > 0 and self.b % 2 == 0 and self.c % self.a == 0

if __name__ == '__main__':
    checker = AttributeChecker(5, 4, 10)
    print(checker.is_valid())