def flatten_boolean_logic(nested_bools):
    def recursive_flatten(data):
        if isinstance(data, bool):
            return data
        elif isinstance(data, list) or isinstance(data, tuple):
            flattened = [recursive_flatten(item) for item in data]
            if not any(flattened):
                return False
            elif all(flattened):
                return True
            else:
                return flattened
        else:
            raise TypeError("Unsupported data type encountered")

    return recursive_flatten(nested_bools)

if __name__ == '__main__':
    test_structure_1 = [True, [False, True], [True, [False, False]], True]
    test_structure_2 = [True, [False, [True, [False, True]]], True]
    test_structure_3 = [False, [True, [False, [True, [False, False]]]]]

    result_1 = flatten_boolean_logic(test_structure_1)
    print(f"Result 1: {result_1}")

    result_2 = flatten_boolean_logic(test_structure_2)
    print(f"Result 2: {result_2}")

    result_3 = flatten_boolean_logic(test_structure_3)
    print(f"Result 3: {result_3}")