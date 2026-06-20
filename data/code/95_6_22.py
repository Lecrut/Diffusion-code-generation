class AttributeChecker:
    def __init__(self, a, b, c):
        if not isinstance(a, int) or a <= 0:
            raise ValueError("a must be a positive integer")
        if not isinstance(b, int) or b % 2 != 0:
            raise ValueError("b must be an even integer")
        if not isinstance(c, int) or c % a != 0:
            raise ValueError("c must be divisible by a")
        self.a = a
        self.b = b
        self.c = c

    def check_attributes(self):
        return True

if __name__ == '__main__':
    try:
        checker = AttributeChecker(5, 4, 10)
        print(checker.check_attributes())
    except ValueError as e:
        print(e)