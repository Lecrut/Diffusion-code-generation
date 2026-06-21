def validate_combination(first, second, third):
    is_positive = first > 0
    is_even = second % 2 == 0
    product_of_first_two = first * second
    is_divisible = product_of_first_two != 0 and third % product_of_first_two == 0
    return is_positive and is_even and is_divisible

if __name__ == '__main__':
    sample_first = 3
    sample_second = 6
    sample_third = 18
    outcome = validate_combination(sample_first, sample_second, sample_third)
    print(outcome)