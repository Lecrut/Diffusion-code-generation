from typing import Any
class DynamicConditionChecker:
    @staticmethod
    def check_condition(value: Any) -> bool:
        return isinstance(value, (int, float))
if __name__ == '__main__':
    checker = DynamicConditionChecker()
    test_cases = [42, 3.14, "string", None]
    for case in test_cases:
        result = checker.check_condition(case)
        print(f"Value {case} is valid: {result}")