from typing import Union

class ValueChecker:
    def check_for_zero(self, value: Union[int, float]) -> bool:
        if not isinstance(value, (int, float)):
            raise ValueError("Unsupported input type")
        return self._is_zero(value)

    def _is_zero(self, value: Union[int, float]) -> bool:
        return value == 0

if __name__ == '__main__':
    checker = ValueChecker()
    sample_values = [0, 1, -1, 0.0, 0.1, -0.1, 2.718, -3.14]
    results = {value: checker.check_for_zero(value) for value in sample_values}
    print(results)