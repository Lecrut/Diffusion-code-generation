def check_both_false(a, b):
    falsy_values = {0, 0.0, False, '', [], (), {}, set(), None}
    a_is_false = a in falsy_values
    b_is_false = b in falsy_values
    return a_is_false and b_is_false

if __name__ == '__main__':
    sample_a = None
    sample_b = set()
    outcome = check_both_false(sample_a, sample_b)
    print(outcome)