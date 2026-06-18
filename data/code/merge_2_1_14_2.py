from typing import Any
class DynamicConditionChecker:
    def check_condition(self, value: Any) -> bool:
        return isinstance(value, int) and 0 <= value < 100
if __name__ == '__main__':
    checker = DynamicConditionChecker()
    sample_values = [50, -5, "text", True]
    for val in sample_values:
        result = checker.check_condition(val)
        print(f"Value {val}: Condition {'met' if result else 'not met'}")