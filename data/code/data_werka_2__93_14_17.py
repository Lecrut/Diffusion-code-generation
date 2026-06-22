def both_flags_false(flag_a, flag_b):
    if flag_a:
        return False
    if flag_b:
        return False
    return True

if __name__ == '__main__':
    first_sample = False
    second_sample = False
    outcome = both_flags_false(first_sample, second_sample)
    print(outcome)