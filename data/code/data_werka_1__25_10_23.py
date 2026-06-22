from typing import Union

class ValueChecker:
    def check_for_zero(self, value: Union[int, float]) -> bool:
        return value == 0

if __name__ == '__main__':
    checker = ValueChecker()
    sample_values = [0, 1, -1, 0.0, 0.1]
    results = {value: checker.check_for_zero(value) for value in sample_values}
    print(results)