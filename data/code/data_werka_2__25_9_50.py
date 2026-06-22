from typing import Union

class ValueChecker:
    ZERO_VALUES = {0, 0.0}
    
    def check_for_zero(self, value: Union[int, float]) -> bool:
        return self._is_zero(value)
    
    @staticmethod
    def _is_zero(value: Union[int, float]) -> bool:
        return value in ValueChecker.ZERO_VALUES

if __name__ == '__main__':
    checker = ValueChecker()
    sample_values = [0, 1, -1, 0.0, 0.1, -0.1, 100, -0.0001]
    results = {value: checker.check_for_zero(value) for value in sample_values}
    print(results)