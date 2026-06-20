def is_mutually_exclusive_set(boolean_values):
    return sum(boolean_values) == 1

if __name__ == '__main__':
    sample_set = {True, False, False}
    print(is_mutually_exclusive_set(sample_set))