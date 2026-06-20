def check_sum_greater_than_difference(num1, num2):
    sum_result = num1 + num2
    difference_result = abs(num1 - num2)
    return sum_result > difference_result

if __name__ == '__main__':
    val_a = 10
    val_b = 5
    final_outcome = check_sum_greater_than_difference(val_a, val_b)
    print(final_outcome)