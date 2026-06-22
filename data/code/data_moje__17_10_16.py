def _get_last_by_index(items):
    if len(items) == 0:
        return None
    return items[len(items) - 1]

def _validate_data_type(items):
    if not isinstance(items, list):
        return False
    return True

def get_last_element(items):
    if not _validate_data_type(items):
        return None
    return _get_last_by_index(items)

if __name__ == '__main__':
    TYPE_CONFIG = {
        "numbers": [1, 2, 3, 4, 5],
        "text": ["hello", "world"],
        "empty": []
    }
    
    test_case_1 = TYPE_CONFIG["numbers"]
    test_case_2 = TYPE_CONFIG["text"]
    test_case_3 = TYPE_CONFIG["empty"]
    
    print(get_last_element(test_case_1))
    print(get_last_element(test_case_2))
    print(get_last_element(test_case_3))