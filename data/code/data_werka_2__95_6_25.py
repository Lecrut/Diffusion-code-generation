class AttributeChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_conditions(self):
        if self.a <= 0:
            return False
        if self.b % 2 != 0:
            return False
        if self.c % self.a != 0:
            return False
        return True

if __name__ == '__main__':
    checker = AttributeChecker(a=2, b=4, c=8)
    result = checker.check_conditions()
    print(result)