def is_mutually_exclusive_set(s):
    true_count = sum((1 for value in s if value))
    return true_count == 1
if __name__ == '__main__':
    sample_set_1 = {True, False}
    sample_set_2 = {False, False}
    sample_set_3 = {True, True}
    sample_set_4 = {}
    print(is_mutually_exclusive_set(sample_set_1))
    print(is_mutually_exclusive_set(sample_set_2))
    print(is_mutually_exclusive_set(sample_set_3))
    print(is_mutually_exclusive_set(sample_set_4))