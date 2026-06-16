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
    def branch(self, condition_op, value_a, value_b):
        if isinstance(value_a, np.ndarray) or isinstance(value_b, np.ndarray):
            func = self._operators.get(condition_op.lower(), None)
            if not func:
                raise ValueError(f"Unsupported operator: {condition_op}")
            return func(np.array(value_a), np.array(value_b))
        else:
            func = self._operators.get(condition_op.lower(), None)
            if not func:
                raise ValueError(f"Unsupported operator: {condition_op}")
            result = func(float(value_a), float(value_b))
            return [result]
if __name__ == '__main__':
    brancher = ConditionalBrancher()
    scalar_result = brancher.branch('gt', 10, 5)
    arr_a = np.array([2.3, 4.7, 9.1])
    arr_b = np.array([1.0, 3.0, 8.0])
    vec_result = brancher.branch('gt', arr_a, arr_b)
    print(f"Scalar result: {scalar_result}")
    print(f"Vectorized result: {vec_result}")