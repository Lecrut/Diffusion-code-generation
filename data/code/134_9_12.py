def assert_single_true(lst):
    if not all(isinstance(x, bool) for x in lst):
        raise ValueError("All elements must be boolean")
    return sum(lst) == 1

if __name__ == '__main__':
    sample_values = [True, False, False]
    print(assert_single_true(sample_values))