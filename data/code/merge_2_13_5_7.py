import sys
def safe_max_value(data):
    if not data:
        return None
    first = data[0]
    try:
        max_val = float('-inf')
        for item in data:
            if isinstance(item, (int, float)) and not isinstance(first, (int, float)):
                return None
            current_max = max(max_val, item)
    except TypeError as e:
        raise ValueError(f"Cannot compare mixed types in sequence. Error details: {e}") from e
    return first
if __name__ == '__main__':
    sample_list_1 = [3, 5, -2]
    sample_list_2 = []
    sample_list_3 = ['a', 'b']                                                                                 
    test_cases = [sample_list_1, sample_list_2, None]
    for i, case in enumerate(test_cases):
        try:
            result = safe_max_value(case)
            print(f"Case {i}: Result is {result}")
        except Exception as e:
            print(f"Case {i} Error: {e}")