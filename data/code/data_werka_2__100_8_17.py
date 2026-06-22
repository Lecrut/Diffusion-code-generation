def sum_exceeds_difference(left, right):
    additive_result = left + right
    subtractive_result = left - right
    return additive_result > subtractive_result

if __name__ == '__main__':
    first_operand = 2
    second_operand = 9
    comparison_outcome = sum_exceeds_difference(first_operand, second_operand)
    print(comparison_outcome)