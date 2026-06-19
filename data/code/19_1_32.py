class ConditionChecker:

    def check_condition(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError('Both inputs must be numbers')
        return a == b
if __name__ == '__main__':
    checker = ConditionChecker()
    try:
        print(checker.check_condition(10, 10))
        print(checker.check_condition(3.5, 3.5))
        print(checker.check_condition('a', 'a'))
    except ValueError as e:
        print(e)