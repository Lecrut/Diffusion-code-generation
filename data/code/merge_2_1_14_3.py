from typing import Any
class DynamicConditionChecker:
    def check_condition(self, value: Any) -> bool:
        return isinstance(value, int) and 0 <= value <= 100
if __name__ == '__main__':
    checker = DynamicConditionChecker()
    test_cases = [42, -5, "text", None, True]
    for case in test_cases:
        result = checker.check_condition(case)
        print(f"Value {case!r}: Condition met? {result}")