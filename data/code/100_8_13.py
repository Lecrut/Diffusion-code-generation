def validate_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both inputs must be numbers")
    return True

def check_sum_greater_than_difference(a, b):
    if not validate_numbers(a, b):
        return False
    sum_result = a + b
    difference_result = abs(a - b)
    return sum_result > difference_result

if __name__ == '__main__':
    val_a = 10
    val_b = 5
    final_outcome = check_sum_greater_than_difference(val_a, val_b)
    print(final_outcome)