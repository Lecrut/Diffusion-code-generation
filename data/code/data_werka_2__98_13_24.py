def evaluate_conditions(first: int, second: int, third: int) -> bool:
    is_first_positive = first > 0
    is_second_positive = second > 0
    is_third_positive = third > 0
    positive_count = sum([is_first_positive, is_second_positive, is_third_positive])
    return positive_count >= 2

if __name__ == '__main__':
    val_a = 10
    val_b = -5
    val_c = -8
    final_result = evaluate_conditions(val_a, val_b, val_c)
    print(final_result)