class ProportionChecker:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def is_proportional(self, num3, num4):
        if self.num2 == 0 or num4 == 0:
            return False
        return (self.num1 / self.num2) == (num3 / num4)

if __name__ == '__main__':
    a = 10
    b = 5
    c = 20
    d = 10
    checker = ProportionChecker(a, b)
    print(f"Are {a}, {b}, {c}, and {d} in proportion? {checker.is_proportional(c, d)}")