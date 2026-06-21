def evaluate_flags(flag_set):
    return (not flag_set[0] and flag_set[1]) or (flag_set[2] and not flag_set[3])

if __name__ == '__main__':
    sample_flags = (True, False, True, False)
    print(evaluate_flags(sample_flags))