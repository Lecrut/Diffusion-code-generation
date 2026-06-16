import numpy as np
class ConditionalBrancher:
    def __init__(self):
        self._operators = {
            '>': lambda a, b: (a > b),
            '<': lambda a, b: (a < b),
            '>=': lambda a, b: (a >= b),
            '<=': lambda a, b: (a <= b)
        }
    def branch(self, condition_op, value_a, value_b):
        if isinstance(value_a, np.ndarray) or isinstance(value_b, np.ndarray):
            op_func = self._operators.get(condition_op)
            result_mask = op_func(np.asarray(value_a), np.asarray(value_b))
            return np.where(result_mask, True, False).tolist()
        else:
            if condition_op not in self._operators:
                raise ValueError(f"Unsupported operator '{condition_op}'. Supported: {list(self._operators.keys())}")
            op_func = self._operators[condition_op]
            result_bool = op_func(value_a, value_b)
            return [result_bool]
if __name__ == '__main__':
    brancher = ConditionalBrancher()
    scalar_result = brancher.branch('>', 10, 5)
    arr_a = np.array([2.3, 4.7, 6.9])
    arr_b = np.array([1.1, 3.3, 5.5])
    vector_result = brancher.branch('>', arr_a, arr_b)
    print(f"Scalar result: {scalar_result}")
    print(f"Vectorized result: {vector_result}")