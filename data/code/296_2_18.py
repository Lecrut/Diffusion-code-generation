class ProportionChecker:
    def __init__(self, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot calculate proportion when the second number is zero")
        self.num1 = num1
        self.num2 = num2

    def check_proportion(self, a, b):
        return (a * self.num2) == (b * self.num1)

if __name__ == '__main__':
    a = 10
    b = 5
    c = 6
    d = 3
    checker = ProportionChecker(a, b)
    print(f"Is the proportion of {a}:{b} equal to {c}:{d}? {checker.check_proportion(c, d)}")