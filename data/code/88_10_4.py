class ConditionChecker:
    def __init__(self, condition_a, condition_b):
        self.condition_a = condition_a
        self.condition_b = condition_b
    
    def check_conditions(self):
        return self.condition_a and self.condition_b

if __name__ == '__main__':
    checker = ConditionChecker(True, False)
    result = checker.check_conditions()
    print(result)