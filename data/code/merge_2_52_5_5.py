def get_last_item(container):
    if isinstance(container, list):
        return container[-1] if container else None
    elif isinstance(container, tuple):
        return container[-1] if container else None
    elif isinstance(container, str):
        return container[-1] if container else None
    elif isinstance(container, set):
        sorted_items = sorted(list(container))
        return sorted_items[-1] if sorted_items else None
    elif isinstance(container, dict):
        keys_list = list(container.keys())
        return keys_list[-1] if keys_list else None
    else:
        raise TypeError(f"Unsupported container type: {type(container).__name__}. Supported types are list, tuple, str, set, and dict.")
if __name__ == '__main__':
    test_cases = [
        {"container": ["apple", "banana", "cherry"], "expected": "cherry"},
        {"container": (10, 20), "expected": 20},
        {"container": "python", "expected": "n"},
        {"container": {5, 3, 8}, "expected": 8},                                 
        {"container": {}, "expected": None},
    ]
    for test in test_cases:
        try:
            result = get_last_item(test["container"])
            status = "PASS" if result == test["expected"] else f"FAIL (got {result})"
            print(f"{test['container']} -> {status}")
        except Exception as e:
            print(f"{test['container']} -> ERROR ({e})")
    try:
        get_last_item([1, 2]) + "string appended to list"                                                                                                                                                                              
    except TypeError as e:
        print(f"Caught expected TypeError for invalid container: {e}")
    try:
        get_last_item(12345)
    except TypeError:
        pass