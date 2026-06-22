class ProportionChecker:
    def __init__(self, num1, num2, num3):
        self.numbers = [num1, num2, num3]

    def are_in_proportion(self):
        if len(self.numbers) < 4:
            raise ValueError("At least four numbers are required to check proportion")
        
        ratio = self.numbers[1] / self.numbers[0]
        for i in range(2, len(self.numbers)):
            if self.numbers[i] / self.numbers[i-1] != ratio:
                return False
        return True

if __name__ == '__main__':
    a = 6
    b = 8
    c = 9
    d = 12
    checker = ProportionChecker(a, b, c, d)
    print(f"Are {a}, {b}, {c}, and {d} in proportion? {checker.are_in_proportion()}")