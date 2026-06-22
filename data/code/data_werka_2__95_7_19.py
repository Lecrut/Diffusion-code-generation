POSITIVE_THRESHOLD = 0

def validate_combined_conditions(first_val, second_val, third_val):
    is_positive = first_val > POSITIVE_THRESHOLD
    is_even = second_val % 2 == 0
    product = first_val * second_val
    is_divisible = product != 0 and third_val % product == 0
    return is_positive and is_even and is_divisible

if __name__ == '__main__':
    val_a = 3
    val_b = 6
    val_c = 18
    final_result = validate_combined_conditions(val_a, val_b, val_c)
    print(final_result)