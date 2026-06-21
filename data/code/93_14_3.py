def check_both_false(first_flag, second_flag):
    is_first_false = not first_flag
    is_second_false = not second_flag
    return is_first_false and is_second_false

if __name__ == '__main__':
    sample_a = False
    sample_b = False
    outcome = check_both_false(sample_a, sample_b)
    print(outcome)