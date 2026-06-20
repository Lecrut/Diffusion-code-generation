def check_sum_greater_than_difference(a, b):
    try:
        sum_result = a + b
        difference_result = abs(a - b)
        return sum_result > difference_result
    except TypeError as e:
        print(f"Invalid input: {e}")
        return None

if __name__ == '__main__':
    val_a = 10
    val_b = 5
    final_outcome = check_sum_greater_than_difference(val_a, val_b)
    print(final_outcome)