class ConditionChecker:

    def __init__(self):
        self.error_messages = {'zero_division': 'The second number cannot be zero.'}

    def check(self, num1, num2):
        if num2 == 0:
            raise ValueError(self.error_messages['zero_division'])
        return num1 % num2 == 0
if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check(15, 3))
    print(checker.check(15, 4))
    try:
        print(checker.check(15, 0))
    except ValueError as e:
        print(e)