class EqualityChecker:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def check(self):
        return self.a == self.b

if __name__ == '__main__':
    ec1 = EqualityChecker(10, 10)
    ec2 = EqualityChecker("hello", "world")
    ec3 = EqualityChecker([1, 2, 3], [1, 2, 3])
    ec4 = EqualityChecker({"a": 1}, {"a": 1})

    print(ec1.check())  # True
    print(ec2.check())  # False
    print(ec3.check())  # True
    print(ec4.check())  # True