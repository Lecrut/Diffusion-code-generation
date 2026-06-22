def is_condition_true(a, b):
    comparison_table = {(42, 42): True, ('hello', 'hello'): True, (3.14, 3.14): True}
    key = (a, b)
    return comparison_table.get(key, a == b)
if __name__ == '__main__':
    sample_a = 42
    sample_b = 42
    result = is_condition_true(sample_a, sample_b)
    print(result)