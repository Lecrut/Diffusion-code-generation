import numpy as np
class ConditionalBranch:
    def __init__(self):
        self.conditions = []
    def add_condition(self, lhs, rhs, operator='gt'):
        if not isinstance(operator, str) or operator not in ('eq', 'lt', 'le', 'ge', 'neq', 'gt'):
            raise ValueError("Unsupported operator")
        cond_func = {
            'eq': lambda x: np.equal(x[0], x[1]),
            'lt': lambda x: np.less(x[0], x[1]),
            'le': lambda x: np.less_equal(x[0], x[1]),
            'ge': lambda x: np.greater_equal(x[0], x[1]),
            'neq': lambda x: np.not_equal(x[0], x[1]),
            'gt': lambda x: np.greater(x[0], x[1])
        }.get(operator, None)
        if cond_func is not None:
            self.conditions.append((cond_func, lhs, rhs))
    def evaluate(self):
        results = []
        for func, a, b in self.conditions:
            try:
                result = func([a, b])
                results.append(result)
            except Exception as e:
                raise RuntimeError(f"Error evaluating condition {e}")
        return np.stack(results, axis=0)
if __name__ == '__main__':
    data_a = np.array([[1.5], [2.3], [4.7]])
    data_b = np.array([1.0, 2.0, 5.0])
    brancher = ConditionalBranch()
    brancher.add_condition(data_a[0][0], data_b[0], 'gt')
    brancher.add_condition(np.array([1.6]), np.array([2.5]), 'ge')
    try:
        results = brancher.evaluate()
        print("Comparison Results:")
        for i, res in enumerate(results):
            if isinstance(res, np.ndarray) and len(res.shape) > 0:
                print(f"Condition {i}: {res.flatten()}")
            else:
                print(f"Condition {i}: {res}")
    except Exception as e:
        print(f"Execution Error: {e}")