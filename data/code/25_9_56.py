from typing import Union

class ValueChecker:
    def check_for_zero(self, value: Union[int, float]) -> bool:
        return self._is_zero(value)

    def _is_zero(self, value: Union[int, float]) -> bool:
        zero_threshold = 1e-9
        return abs(value) < zero_threshold

if __name__ == '__main__':
    checker = ValueChecker()
    sample_values = [0, -0.000000001, 0.000000001, 100, -100, 0.5]
    results = {value: checker.check_for_zero(value) for value in sample_values}
    print(results)