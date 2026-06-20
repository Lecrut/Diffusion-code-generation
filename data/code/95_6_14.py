class AttributeChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def validate_input(self):
        if not isinstance(self.a, int) or self.a <= 0:
            raise ValueError("a must be a positive integer")
        if not isinstance(self.b, int) or self.b % 2 != 0:
            raise ValueError("b must be an even integer")
        if not isinstance(self.c, int) or self.c % self.a != 0:
            raise ValueError("c must be divisible by a")

    def check_attributes(self):
        self.validate_input()
        return True

if __name__ == '__main__':
    try:
        checker = AttributeChecker(5, 4, 10)
        print(checker.check_attributes())
    except ValueError as e:
        print(e)