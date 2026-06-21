class ConditionChecker:
    VALID_TYPES = (bool, int, float, str, list, tuple, set, dict, type(None))
    TRUTHY_THRESHOLD = 1

    @staticmethod
    def _is_truthy(value):
        if isinstance(value, bool):
            return value
        if isinstance(value, (int, float)):
            return value != 0
        if isinstance(value, (str, list, tuple, set, dict)):
            return len(value) > 0
        if value is None:
            return False
        return bool(value)

    def evaluate(self, parameters):
        if not parameters:
            return True
        for key, value in parameters.items():
            if not self._is_truthy(value):
                return False
        return True

if __name__ == '__main__':
    checker = ConditionChecker()
    sample_data = {"count": 5, "name": "test", "active": True}
    result = checker.evaluate(sample_data)
    print(result)
    empty_data = {}
    empty_result = checker.evaluate(empty_data)
    print(empty_result)
    falsy_data = {"count": 0, "name": "", "active": False}
    falsy_result = checker.evaluate(falsy_data)
    print(falsy_result)