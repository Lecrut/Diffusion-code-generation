def evaluate_and_gate(left_operand, right_operand):
    if not isinstance(left_operand, bool) or not isinstance(right_operand, bool):
        raise ValueError("Operands must be boolean")
    computed_result = left_operand and right_operand
    return computed_result

if __name__ == '__main__':
    val_x = False
    val_y = True
    outcome = evaluate_and_gate(val_x, val_y)
    print(outcome)