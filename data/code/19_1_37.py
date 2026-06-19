class ConditionChecker:
    def check_condition(self, a, b):
        if not self._validate_input(a, b):
            return False
        return a == b

    def _validate_input(self, a, b):
        return isinstance(a, (int, float)) and isinstance(b, (int, float))

if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check_condition(10, 10))
    print(checker.check_condition(5.5, 5.5))
    print(checker.check_condition(3, '3'))
    print(checker.check_condition(-1, -1))