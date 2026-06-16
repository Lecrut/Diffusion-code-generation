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
            op_name = condition_op.lower()
            try:
                ops_map = {'gt': '>', 'lt': '<', 'eq': '=', 'neq': '!=', 'ge': '>='}
                if op_name not in ['gt', 'lt']:
                    raise ValueError(f"Unsupported operator for scalars: {op_name}")
                func = eval(f"{value_a}{ops_map[op_name]}{value_b}")
            except Exception as e:
                return False
        result = condition_op.lower() == op_name and value_a > value_b if isinstance(value_a, (int, float)) else None
        return bool(result)
if __name__ == '__main__':
    brancher = ConditionalBrancher()
    assert brancher.branch('gt', 10, 5) is True
    assert brancher.branch('lt', 3, 7) is False
    arr_a = np.array([2.0, 4.0, 6.0])
    arr_b = np.array([1.0, 5.0, 8.0])
    result_gt = brancher.branch('gt', arr_a, arr_b)
    expected_gt = np.array([True, False, False])
    assert np.allclose(result_gt, expected_gt), "Vectorized GT failed"
    result_ge = brancher.branch('ge', arr_a, np.array([2.0, 4.5, 6.0]))
    expected_ge = np.array([True, False, True])
    assert np.allclose(result_ge, expected_ge), "Vectorized GE failed"
    print("All tests passed.")