def count_elements(lst):
    return len(lst) if isinstance(lst, list) else 0
if __name__ == '__main__':
    test_list = [1, "apple", None, [], {"key": "value"}]
    empty_list = []
    mixed_types = [[], {}, set(), True, False]
    print(count_elements(test_list))
    print(count_elements(empty_list))
    print(count_elements(mixed_types))