NUMERIC_THRESHOLD = 1e-9

def evaluate_sum_vs_difference(left_operand, right_operand):
    if left_operand is None or right_operand is None:
        raise ValueError("Operands cannot be None")
    total = left_operand + right_operand
    gap = left_operand - right_operand
    return total - gap > NUMERIC_THRESHOLD

if __name__ == '__main__':
    first_val = 7
    second_val = 3
    comparison_result = evaluate_sum_vs_difference(first_val, second_val)
    print(comparison_result)