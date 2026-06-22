class ConditionChecker:
    OPERATORS = {
        "eq": lambda a, b: a == b,
        "gt": lambda a, b: a > b,
        "lt": lambda a, b: a < b,
        "gte": lambda a, b: a >= b,
        "lte": lambda a, b: a <= b,
        "neq": lambda a, b: a != b,
    }

    def evaluate(self, conditions):
        if not conditions:
            return True
        for key, rule in conditions.items():
            if not isinstance(rule, (list, tuple)) or len(rule) != 2:
                raise ValueError(f"Invalid rule format for key '{key}': {rule}")
            expected_value, operator_name = rule
            if operator_name not in self.OPERATORS:
                raise ValueError(f"Unsupported operator '{operator_name}' for key '{key}'")
            actual_value = conditions.get(key)
            if not self.OPERATORS[operator_name](actual_value, expected_value):
                return False
        return True

if __name__ == '__main__':
    checker = ConditionChecker()
    config1 = {"age": (18, "gte"), "status": ("active", "eq"), "score": (100, "lte")}
    result1 = checker.evaluate(config1)
    print(f"Result 1: {result1}")
    config2 = {"age": (20, "gte"), "status": ("inactive", "eq"), "score": (100, "lte")}
    result2 = checker.evaluate(config2)
    print(f"Result 2: {result2}")
    config3 = {"age": (10, "gte"), "status": ("active", "eq"), "score": (50, "lte")}
    result3 = checker.evaluate(config3)
    print(f"Result 3: {result3}")
    config4 = {}
    result4 = checker.evaluate(config4)
    print(f"Result 4: {result4}")