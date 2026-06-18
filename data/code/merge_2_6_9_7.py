import numpy as np
class ConditionalBrancher:
    def __init__(self):
        self._operators = {
            'gt': lambda a, b: a > b,
            'lt': lambda a, b: a < b,
            'eq': lambda a, b: a == b,
            'neq': lambda a, b: a != b,
            'ge': lambda a, b: a >= b,
            'le': lambda a, b: a <= b,
        }
    def branch(self, condition_func):
        return condition_func()
def greater_than(a, b):
    if isinstance(a, np.ndarray) and isinstance(b, (int, float)):
        result = a > b.astype(np.float64)
    elif isinstance(a, int) or isinstance(a, float):
        result = a > b
    else:
        raise TypeError("Unsupported types for comparison")
    return result
if __name__ == '__main__':
    data_a = np.array([10.5, 20.3, 30.7])
    threshold = 15
    brancher = ConditionalBrancher()
    def check_gt():
        if isinstance(data_a[0], (int, float)):
            return greater_than(10.5, 15)
        else:
            result_array = data_a > threshold
            for val in result_array:
                print(val)
    brancher.branch(check_gt)