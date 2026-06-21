def flatten_boolean_logic(nested_bools):
    if isinstance(nested_bools, bool):
        return nested_bools
    elif isinstance(nested_bools, list) or isinstance(nested_bools, tuple):
        flat_list = [flatten_boolean_logic(item) for item in nested_bools]
        if all(isinstance(item, bool) for item in flat_list):
            return any(flat_list)
        else:
            raise ValueError("Nested structure contains non-boolean values")
    else:
        raise TypeError("Unsupported data type encountered")

if __name__ == '__main__':
    test_structure_1 = [True, [False, True], [True, [False, False]], True]
    test_structure_2 = [True, [False, [True, [False, True]]], True]
    test_structure_3 = [False, [True, [False, [True, [False, False]]]]]
    
    try:
        result_1 = flatten_boolean_logic(test_structure_1)
        print(f"Result 1: {result_1}")
        
        result_2 = flatten_boolean_logic(test_structure_2)
        print(f"Result 2: {result_2}")
        
        result_3 = flatten_boolean_logic(test_structure_3)
        print(f"Result 3: {result_3}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")