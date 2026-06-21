from typing import Union

class ValueChecker:
    _ZERO_VALUES = {0, 0.0}

    def check_for_zero(self, value: Union[int, float]) -> bool:
        return self._is_zero(value)

    @staticmethod
    def _is_zero(value: Union[int, float]) -> bool:
        if isinstance(value, (int, float)):
            return value in ValueChecker._ZERO_VALUES
        raise ValueError("Unsupported input type")

if __name__ == '__main__':
    checker = ValueChecker()
    sample_values = [0, 1, -1, 0.0, 0.1, -0.1, 10, -10, 3.14, -3.14]
    results = {value: checker.check_for_zero(value) for value in sample_values}
    print(results)