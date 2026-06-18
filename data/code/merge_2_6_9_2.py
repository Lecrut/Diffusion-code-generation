import numpy as np
class GreaterThanOperator:
    def __init__(self):
        self._op = lambda a, b: a > b
    def __call__(self, left_operand, right_operand):
        return self._op(left_operand, right_operand)
def conditional_branch(value, condition_result, true_value=None, false_value=0.0):
    if isinstance(condition_result, np.ndarray):
        result = np.where(condition_result, true_value, false_value)
    else:
        result = true_value if condition_result else false_value
    return result
if __name__ == '__main__':
    gt_op = GreaterThanOperator()
    scalar_a = 10.5
    scalar_b = 3.2
    vector_x = np.array([1, 4, 7, 9])
    vector_y = np.array([2, 6, 8, 12])
    result_scalar = conditional_branch(scalar_a, gt_op.__call__(scalar_a, scalar_b), true_value=100.0)
    result_vector = conditional_branch(vector_x, lambda x: gt_op(x, vector_y), 
                                      true_value=np.full_like(vector_x, 999.0))
    print(f"Scalar Result: {result_scalar}")