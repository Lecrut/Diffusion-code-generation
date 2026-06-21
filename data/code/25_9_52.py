from typing import Union

class ValueChecker:
    def __init__(self):
        self.zero_map = {0: True, 0.0: True}
    
    def check_for_zero(self, value: Union[int, float]) -> bool:
        return value in self.zero_map

if __name__ == '__main__':
    checker = ValueChecker()
    sample_values = [0, 1, -1, 0.0, 0.1, -0.1, 2.0, -0.0]
    results = {value: checker.check_for_zero(value) for value in sample_values}
    print(results)