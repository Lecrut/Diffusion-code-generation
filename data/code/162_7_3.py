def map_dictionary_values(input_dict, mapping_function):
    output_dict = {}
    for key, value in input_dict.items():
        output_dict[key] = mapping_function(value)
    return output_dict
if __name__ == '__main__':
    def double(x):
        return x * 2
    dict1 = {"a": 1, "b": 2, "c": 3}
    result1 = map_dictionary_values(dict1, double)
    print(f"Test Case 1 Input: {dict1}")
    print(f"Test Case 1 Mapping Function: double")
    print(f"Test Case 1 Result: {result1}")
    assert result1 == {"a": 2, "b": 4, "c": 6}
    dict2 = {"x": 10, "y": 20, "z": 30}
    result2 = map_dictionary_values(dict2, double)
    print(f"\nTest Case 2 Input: {dict2}")
    print(f"Test Case 2 Mapping Function: double")
    print(f"Test Case 2 Result: {result2}")
    assert result2 == {"x": 20, "y": 40, "z": 60}
    dict3 = {"score": 50, "count": 100}
    def add_ten(x):
        return x + 10
    result3 = map_dictionary_values(dict3, add_ten)
    print(f"\nTest Case 3 Input: {dict3}")
    print(f"Test Case 3 Mapping Function: add_ten")
    print(f"Test Case 3 Result: {result3}")
    assert result3 == {"score": 60, "count": 110}
    dict4 = {}
    result4 = map_dictionary_values(dict4, double)
    print(f"\nTest Case 4 Input: {dict4}")
    print(f"Test Case 4 Mapping Function: double")
    print(f"Test Case 4 Result: {result4}")
    assert result4 == {}
    dict5 = {"empty": 0}
    def multiply_by_three(x):
        return x * 3
    result5 = map_dictionary_values(dict5, multiply_by_three)
    print(f"\nTest Case 5 Input: {dict5}")
    print(f"Test Case 5 Mapping Function: multiply_by_three")
    print(f"Test Case 5 Result: {result5}")
    assert result5 == {"empty": 0}