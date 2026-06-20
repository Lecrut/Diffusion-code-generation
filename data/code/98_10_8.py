class ConditionChecker:
    def __init__(self):
        self.conditions = {}

    def add_condition(self, name, condition):
        self.conditions[name] = condition

    def check_all(self):
        return all(self.conditions.values())

if __name__ == '__main__':
    checker = ConditionChecker()
    checker.add_condition('a', True)
    checker.add_condition('b', False)
    checker.add_condition('c', True)
    
    result = checker.check_all()
    print(f"Condition 'a': {checker.conditions['a']}")
    print(f"Condition 'b': {checker.conditions['b']}")
    print(f"Condition 'c': {checker.conditions['c']}")
    print(f"All conditions met: {result}")