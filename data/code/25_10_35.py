from typing import Any

class ValueChecker:
    def check_for_zero(self, value: Any) -> bool:
        return value == 0

if __name__ == '__main__':
    checker = ValueChecker()
    sample_values = [0, 1, -1, None, False, '0', 0.0]
    for value in sample_values:
        print(f"Is {value} zero? {checker.check_for_zero(value)}")