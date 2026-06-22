def compute_digit_sum(number):
    if number < 0:
        raise ValueError("Input must be non-negative")
    if number == 0:
        return 0
    last_digit = number % 10
    remaining_number = number // 10
    recursive_result = compute_digit_sum(remaining_number)
    return last_digit + recursive_result

if __name__ == '__main__':
    sample_one = 409
    sample_two = 0
    sample_three = 99999
    print(compute_digit_sum(sample_one))
    print(compute_digit_sum(sample_two))
    print(compute_digit_sum(sample_three))