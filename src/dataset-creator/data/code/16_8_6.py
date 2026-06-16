def count_elements(lst):
    return len(lst) if isinstance(lst, list) else 0
if __name__ == '__main__':
    test_list = [1, "hello", None, [], {"key": "val"}, True]
    print(count_elements(test_list))
    empty_list = []
    print(f"Empty count: {count_elements(empty_list)}")