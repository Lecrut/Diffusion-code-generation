from typing import Any
class DynamicConditionChecker:
    @classmethod
    def evaluate_condition(cls, value: Any) -> bool:
        return isinstance(value, (int, float)) and value > 5
if __name__ == '__main__':
    checker_instance = DynamicConditionChecker()
    test_cases = [
        ("Integer greater than 5", "10"),
        ("Float less than or equal to 5", "-2.5"),
        ("String input", "hello"),
        ("Zero value", "0"),
        ("Boolean true", True),
    ]
    for description, sample_value in test_cases:
        try:
            converted_value = int(sample_value) if '.' not in str(sample_value) else float(sample_value)
            result = checker_instance.evaluate_condition(converted_value)
            print(f"{description}: {result}")
        except ValueError:
            result = False
            print(f"{description}: {result}")
    manual_test_value = 30
    final_check_result = checker_instance.evaluate_condition(manual_test_value)
    assert final_check_result is True, "Manual test failed"