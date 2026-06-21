from typing import Union

class ValueChecker:
    def check_for_zero(self, value: Union[int, float]) -> bool:
        self._validate_input(value)
        return value == 0
    
    def _validate_input(self, value: Union[int, float]) -> None:
        if not isinstance(value, (int, float)):
            raise ValueError("Input must be an integer or a float")

if __name__ == '__main__':
    checker = ValueChecker()
    sample_values = [0, 1.5, -2.3, 0.0, 0.0001, -0.0001]
    results = {value: checker.check_for_zero(value) for value in sample_values}
    print(results)