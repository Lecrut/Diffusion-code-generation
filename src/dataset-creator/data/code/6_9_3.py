import numpy as np
class ConditionalBrancher:
    def __init__(self):
        self._operators = {
            'gt': lambda a, b: (a > b),
            'lt': lambda a, b: (a < b),
            'ge': lambda a, b: (a >= b),
            'le': lambda a, b: (a <= b)
        }
    def branch(self, condition_key, value_a, value_b):
        if isinstance(value_a, np.ndarray) or isinstance(value_b, np.ndarray):
            op_func = self._operators.get(condition_key.lower(), None)
            if not op_func:
                raise ValueError(f"Unsupported operator key: {condition_key}")
            return op_func(np.asarray(value_a), np.asarray(value_b))
        else:
            op_func = self._operators.get(condition_key.lower(), None)
            if not op_func:
                raise ValueError(f"Unsupported operator key: {condition_key}")
            result = op_func(float(value_a), float(value_b))
            return int(result)
if __name__ == '__main__':
    brancher = ConditionalBrancher()
    scalar_result_gt = brancher.branch('gt', 10, 5)
    print(f"Scalar GT (10 > 5): {scalar_result_gt}")
    arr_a = np.array([1.0, 2.0, 3.0])
    arr_b = np.array([4.0, 6.0, 8.0])
    vec_result_lt = brancher.branch('lt', arr_a, arr_b)
    print(f"Vector LT result: {vec_result_lt}")
    def custom_op(a, b): return a > b or a < b