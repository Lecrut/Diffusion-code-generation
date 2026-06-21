class ConditionChecker:

    def __init__(self):
        self.messages = {'zero_division': 'The second number cannot be zero.'}

    def check(self, num1, num2):
        if num2 == 0:
            raise ValueError(self.messages['zero_division'])
        return num1 % num2 == 0
if __name__ == '__main__':
    checker = ConditionChecker()
    try:
        print(checker.check(25, 5))
        print(checker.check(25, 4))
        print(checker.check(25, 0))
    except ValueError as e:
        print(e)