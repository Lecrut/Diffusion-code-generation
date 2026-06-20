def check_sum_greater_than_difference(a, b):
    return (a + b) > abs(a - b)

if __name__ == '__main__':
    val_a = 10
    val_b = 5
    final_outcome = check_sum_greater_than_difference(val_a, val_b)
    print(final_outcome)