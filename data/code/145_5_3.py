def safe_evaluate_boolean_structure(nested_bools):
    result = True
    for item in nested_bools:
        if isinstance(item, bool):
            result = result and item
        elif isinstance(item, list):
            sub_result = True
            for sub_item in item:
                if isinstance(sub_item, list):
                    sub_result = sub_result and safe_evaluate_boolean_structure(sub_item)
                elif isinstance(sub_item, bool):
                    sub_result = sub_result and sub_item
                else:
                    sub_result = False
            result = result and sub_result
        elif isinstance(item, dict):
            sub_result = True
            for key, value in item.items():
                if isinstance(value, list):
                    sub_result = sub_result and safe_evaluate_boolean_structure([value])
                elif isinstance(value, bool):
                    sub_result = sub_result and value
                else:
                    sub_result = False
            result = result and sub_result
        else:
            result = False
    return result
if __name__ == '__main__':
    test_structure_1 = [True, [False, True], [True, [False, False]], True]
    test_structure_2 = {
        "a": True,
        "b": [False, True],
        "c": {
            "d": False,
            "e": [True]
        }
    }
    test_structure_3 = [True, [False, [True, [False, True]]], False]
    print(f"Test 1 result: {safe_evaluate_boolean_structure(test_structure_1)}")
    print(f"Test 2 result: {safe_evaluate_boolean_structure(test_structure_2)}")
    print(f"Test 3 result: {safe_evaluate_boolean_structure(test_structure_3)}")