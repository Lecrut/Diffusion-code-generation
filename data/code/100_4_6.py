class GreaterThanChecker:
    def is_greater(self, x, y):
        return x > y

if __name__ == '__main__':
    checker = GreaterThanChecker()
    print(checker.is_greater(5, 3))
    print(checker.is_greater(2, 4))