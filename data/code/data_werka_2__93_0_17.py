def evaluate_false_conditionality(left_operand, right_operand):
    if not isinstance(left_operand, bool):
        raise ValueError("left_operand must be a boolean")
    if not isinstance(right_operand, bool):
        raise ValueError("right_operand must be a boolean")
    is_left_false = left_operand is False
    is_right_false = right_operand is False
    return is_left_false and is_right_false

if __name__ == '__main__':
    sample_first = False
    sample_second = False
    outcome = evaluate_false_conditionality(sample_first, sample_second)
    print(outcome)