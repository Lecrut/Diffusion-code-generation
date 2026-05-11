def map_dictionary_values(input_dict, mapping_func):
    output_dict = {}
    for key, value in input_dict.items():
        output_dict[key] = mapping_func(value)
    return output_dict
if __name__ == '__main__':
    input1 = {"a": 1, "b": 2, "c": 3}
    def add_one(x):
        return x + 1
    expected1 = {"a": 2, "b": 3, "c": 4}
    result1 = map_dictionary_values(input1, add_one)
    assert result1 == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {result1}"
    print("Test Case 1 Passed")
    input2 = {"name": "Alice", "city": "New York"}
    def to_upper(s):
        return s.upper()
    expected2 = {"name": "ALICE", "city": "NEW YORK"}
    result2 = map_dictionary_values(input2, to_upper)
    assert result2 == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {result2}"
    print("Test Case 2 Passed")
    input3 = {"x": 1, "y": 2, "z": 3}
    def square(x):
        return x * x
    expected3 = {"x": 1, "y": 4, "z": 9}
    result3 = map_dictionary_values(input3, square)
    assert result3 == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {result3}"
    print("Test Case 3 Passed")
    input4 = {}
    def double(x):
        return x * 2
    expected4 = {}
    result4 = map_dictionary_values(input4, double)
    assert result4 == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {result4}"
    print("Test Case 4 Passed")
    input5 = {"list1": [1, 2], "list2": [3, 4]}
    def get_length(lst):
        return len(lst)
    expected5 = {"list1": 2, "list2": 2}
    result5 = map_dictionary_values(input5, get_length)
    assert result5 == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {result5}"
    print("Test Case 5 Passed")