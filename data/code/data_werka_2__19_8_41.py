class ConditionChecker:
    DIVISIBILITY_THRESHOLD = 0

    def check(self, num1, num2):
        if num2 == self.DIVISIBILITY_THRESHOLD:
            raise ValueError('The second number cannot be zero.')
        return num1 % num2 == 0

if __name__ == '__main__':
    checker = ConditionChecker()
    result = checker.check(25, 5)
    print(result)
    result = checker.check(25, 4)
    print(result)
    try:
        result = checker.check(25, 0)
        print(result)
    except ValueError as e:
        print(e)