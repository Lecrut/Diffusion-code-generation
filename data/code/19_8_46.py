class ConditionChecker:
    DIVISIBILITY_THRESHOLD = 0

    def check(self, num1, num2):
        if num2 == self.DIVISIBILITY_THRESHOLD:
            raise ValueError('The second number cannot be zero.')
        return num1 % num2 == 0
if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check(25, 5))
    print(checker.check(25, 4))
    try:
        print(checker.check(25, 0))
    except ValueError as e:
        print(e)