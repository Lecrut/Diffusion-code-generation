def map_dictionary_values(input_dict, mapping_dict):
    result = {}
    for key, value in input_dict.items():
        if key in mapping_dict:
            result[key] = mapping_dict[key]
        else:
            result[key] = value
    return result
if __name__ == '__main__':
    test_case_1_input = {'a': 1, 'b': 2, 'c': 3}
    test_case_1_mapping = {'a': 100, 'c': 300}
    expected_output_1 = {'a': 100, 'b': 2, 'c': 300}
    actual_output_1 = map_dictionary_values(test_case_1_input, test_case_1_mapping)
    assert actual_output_1 == expected_output_1, f"Test Case 1 Failed: Expected {expected_output_1}, Got {actual_output_1}"
    print("Test Case 1 Passed")
    test_case_2_input = {'x': 5, 'y': 6, 'z': 7}
    test_case_2_mapping = {'x': 50, 'z': 70}
    expected_output_2 = {'x': 50, 'y': 6, 'z': 70}
    actual_output_2 = map_dictionary_values(test_case_2_input, test_case_2_mapping)
    assert actual_output_2 == expected_output_2, f"Test Case 2 Failed: Expected {expected_output_2}, Got {actual_output_2}"
    print("Test Case 2 Passed")
    test_case_3_input = {'apple': 1, 'banana': 2, 'cherry': 3}
    test_case_3_mapping = {'apple': 10, 'grape': 40}
    expected_output_3 = {'apple': 10, 'banana': 2, 'cherry': 3}
    actual_output_3 = map_dictionary_values(test_case_3_input, test_case_3_mapping)
    assert actual_output_3 == expected_output_3, f"Test Case 3 Failed: Expected {expected_output_3}, Got {actual_output_3}"
    print("Test Case 3 Passed")
    test_case_4_input = {'p': 10, 'q': 20}
    test_case_4_mapping = {}
    expected_output_4 = {'p': 10, 'q': 20}
    actual_output_4 = map_dictionary_values(test_case_4_input, test_case_4_mapping)
    assert actual_output_4 == expected_output_4, f"Test Case 4 Failed: Expected {expected_output_4}, Got {actual_output_4}"
    print("Test Case 4 Passed")
    test_case_5_input = {}
    test_case_5_mapping = {'a': 1}
    expected_output_5 = {}
    actual_output_5 = map_dictionary_values(test_case_5_input, test_case_5_mapping)
    assert actual_output_5 == expected_output_5, f"Test Case 5 Failed: Expected {expected_output_5}, Got {actual_output_5}"
    print("Test Case 5 Passed")
    test_case_6_input = {'color': 'red', 'size': 'large'}
    test_case_6_mapping = {'color': 'crimson'}
    expected_output_6 = {'color': 'crimson', 'size': 'large'}
    actual_output_6 = map_dictionary_values(test_case_6_input, test_case_6_mapping)
    assert actual_output_6 == expected_output_6, f"Test Case 6 Failed: Expected {expected_output_6}, Got {actual_output_6}"
    print("Test Case 6 Passed")