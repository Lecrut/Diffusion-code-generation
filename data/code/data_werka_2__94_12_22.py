def has_truthy_element(items):
    if not isinstance(items, (list, tuple, set, dict)):
        raise ValueError("Unsupported input type")
    if isinstance(items, dict):
        return any(items.values())
    return any(items)

if __name__ == '__main__':
    TEST_CASES = {
        "zeros": [0, 0, 0],
        "mixed_ints": [0, 5, 0],
        "empty_list": [],
        "none_vals": [None, None],
        "bool_false": [False, False],
        "bool_true": [False, True]
    }
    for label, data in TEST_CASES.items():
        print(has_truthy_element(data))