from typing import Any

class ValueChecker:
    def check_for_zero(self, value: Any) -> bool:
        return self._is_zero(value)

    def _is_zero(self, value: Any) -> bool:
        zero_values = {0, 0.0}
        return value in zero_values

if __name__ == '__main__':
    checker = ValueChecker()
    sample_values = [0, 1, -1, 0.0, 0.1, -0.1, None, "0", False]
    results = {value: checker.check_for_zero(value) for value in sample_values}
    print(results)