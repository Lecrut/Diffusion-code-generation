from typing import Union

class ValueChecker:
    def check_for_zero(self, value: Union[int, float]) -> bool:
        return self._is_zero(value)
    
    def _is_zero(self, value: Union[int, float]) -> bool:
        if isinstance(value, (int, float)):
            return value == 0
        raise ValueError("Unsupported input type")

if __name__ == '__main__':
    checker = ValueChecker()
    sample_values = [0, 1, -1, 0.0, 0.1, -0.1, 100, -0.0001]
    results = {value: checker.check_for_zero(value) for value in sample_values}
    print(results)