import timeit
def validate_item_presence(container, item):
    return item in container
if __name__ == '__main__':
    sample_sets = {10, 20, 30}
    sample_lists = [5, 'a', None]
    sample_tuples = (True, False)
    sample_frozensets = frozenset(['x', 'y'])
    test_item_set = 20
    test_item_list = 'a'
    test_item_tuple = True
    test_item_fs = 'z'
    print(validate_item_presence(sample_sets, test_item_set))
    print(validate_item_presence(sample_lists, test_item_list))
    print(validate_item_presence(sample_tuples, test_item_tuple))
    print(validate_item_presence(sample_frozensets, test_item_fs))
    large_data = set(range(10_000_000))
    time_set_check = timeit.timeit('validate_item_presence(large_data, 5000)', globals=globals(), number=100)
    print(f"Set lookup (10M items): {time_set_check:.4f}s")
    large_list = list(range(10_000_000))
    time_list_check = timeit.timeit('validate_item_presence(large_list, 5000)', globals=globals(), number=1)
    print(f"List lookup (10M items): {time_list_check:.4f}s")