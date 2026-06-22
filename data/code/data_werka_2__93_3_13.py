class FalseChecker:
    FALSE_STATE = (0, 0.0, "", [], {}, None)

    @staticmethod
    def check(x, y):
        return not x and not y

if __name__ == '__main__':
    x = 0
    y = 0
    checker = FalseChecker()
    result = checker.check(x, y)
    print(result)