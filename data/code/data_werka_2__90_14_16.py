def evaluate_logical_or(left_operand, right_operand):
    if left_operand is None:
        raise ValueError("Left operand cannot be None")
    if right_operand is None:
        raise ValueError("Right operand cannot be None")
    if not isinstance(left_operand, (int, float, str, bool, list, dict, tuple, set)):
        raise ValueError("Left operand type not supported")
    if not isinstance(right_operand, (int, float, str, bool, list, dict, tuple, set)):
        raise ValueError("Right operand type not supported")
    return left_operand or right_operand

class OrConditionEvaluator:
    def __init__(self, value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b

    def compute_result(self):
        return self.value_a or self.value_b

if __name__ == '__main__':
    evaluator = OrConditionEvaluator(0, "success")
    result = evaluator.compute_result()
    print(result)
    
    func_result = evaluate_logical_or(False, 42)
    print(func_result)