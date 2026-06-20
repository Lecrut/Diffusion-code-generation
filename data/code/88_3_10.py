class ConditionChecker:
    def __init__(self):
        self.conditions = {
            (True, True): "Both are true",
            (False, True): "First is false",
            (True, False): "Second is false",
            (False, False): "Both are false"
        }

    def check_conditions_met(self, a: bool, b: bool) -> str:
        return self.conditions.get((a, b), "Invalid input")

if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check_conditions_met(True, True))
    print(checker.check_conditions_met(False, True))
    print(checker.check_conditions_met(True, False))
    print(checker.check_conditions_met(False, False))