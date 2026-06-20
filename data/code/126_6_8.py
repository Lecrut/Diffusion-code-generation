class EqualityChecker:
    @staticmethod
    def compare(x, y):
        return x == y

if __name__ == '__main__':
    checker = EqualityChecker()
    x1 = 5
    y1 = 5
    result1 = checker.compare(x1, y1)
    print(f"Checking equality between {x1} and {y1}: {result1}")
    x2 = 10
    y2 = 20
    result2 = checker.compare(x2, y2)
    print(f"Checking equality between {x2} and {y2}: {result2}")