def evaluate_logical_or(first_operand, second_operand):
    if first_operand:
        return first_operand
    return second_operand

if __name__ == '__main__':
    val1 = evaluate_logical_or(0, 42)
    print(val1)
    val2 = evaluate_logical_or(False, "truth")
    print(val2)
    val3 = evaluate_logical_or([], {"key": "value"})
    print(val3)