def all_true(lst):
    return all(lst)
if __name__ == '__main__':
    sample_values = [True, True, True]
    print(all_true(sample_values))
    sample_values = [False, False, False]
    print(all_true(sample_values))
    sample_values = [True, False, True]
    print(all_true(sample_values))