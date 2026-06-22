class ConditionChecker:

    def __init__(self):
        self.conditions = {'equal': lambda x, y: x == y, 'not_equal': lambda x, y: x != y}

    def check_condition(self, a, b):
        return self.conditions['equal'](a, b)
if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check_condition(10, 10))
    print(checker.check_condition(5, 3))
    print(checker.check_condition(-1, -1))
    print(checker.check_condition(0, 0))