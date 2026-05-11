def map_dictionary_values(input_dict, mapping_func):
    output_dict = {}
    for key, value in input_dict.items():
        output_dict[key] = mapping_func(value)
    return output_dict
if __name__ == '__main__':
    test_cases = [
        ({"a": 1, "b": 2, "c": 3}, lambda x: x * 2),
        ({"apple": 5, "banana": 10, "cherry": 15}, lambda x: x + 10),
        ({}, lambda x: x * 2),
        ({"x": "hello", "y": "world"}, lambda s: s.upper()),
        ({"score": 85, "attempts": 3}, lambda s: s - 10),
    ]
    for input_dict, mapping_func in test_cases:
        result = map_dictionary_values(input_dict, mapping_func)
        print(f"Input: {input_dict}")
        print(f"Mapping Function: {mapping_func.__name__ if hasattr(mapping_func, '__name__') else 'lambda'}")
        print(f"Result: {result}")
        print("-" * 20)