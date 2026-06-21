class ConditionChecker:
    DIVISIBILITY_ERROR_MESSAGE = 'The second number cannot be zero.'

    @staticmethod
    def is_divisible(num1, num2):
        if num2 == 0:
            raise ValueError(ConditionChecker.DIVISIBILITY_ERROR_MESSAGE)
        return num1 % num2 == 0

if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.is_divisible(25, 5))
    print(checker.is_divisible(25, 4))
    try:
        print(checker.is_divisible(25, 0))
    except ValueError as e:
        print(e)