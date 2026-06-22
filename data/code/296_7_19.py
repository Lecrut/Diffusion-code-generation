class RatioChecker:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def are_proportional(self):
        return (self.a / self.b).is_integer()

    def simplify_ratio(self):
        gcd = math.gcd(self.a, self.b)
        return (self.a // gcd, self.b // gcd)

if __name__ == '__main__':
    checker = RatioChecker(12, 18)
    print("Are proportional:", checker.are_proportional())
    print("Simplified ratio:", checker.simplify_ratio())