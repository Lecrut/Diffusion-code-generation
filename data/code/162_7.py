def map_dictionary_values(input_dict, mapping_dict):
    result_dict = {}
    for key, value in input_dict.items():
        if key in mapping_dict:
            result_dict[key] = mapping_dict[key]
        else:
            result_dict[key] = value
    return result_dict
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
    test_case_3_input = {'p': 10, 'q': 20}
    test_case_3_mapping = {'r': 100}
    expected_output_3 = {'p': 10, 'q': 20}
    actual_output_3 = map_dictionary_values(test_case_3_input, test_case_3_mapping)
    assert actual_output_3 == expected_output_3, f"Test Case 3 Failed: Expected {expected_output_3}, Got {actual_output_3}"
    print("Test Case 3 Passed")
    test_case_4_input = {}
    test_case_4_mapping = {'a': 1}
    expected_output_4 = {}
    actual_output_4 = map_dictionary_values(test_case_4_input, test_case_4_mapping)
    assert actual_output_4 == expected_output_4, f"Test Case 4 Failed: Expected {expected_output_4}, Got {actual_output_4}"
    print("Test Case 4 Passed")
    test_case_5_input = {'k1': 'v1', 'k2': 'v2'}
    test_case_5_mapping = {'k1': 'new_v1'}
    expected_output_5 = {'k1': 'new_v1', 'k2': 'v2'}
    actual_output_5 = map_dictionary_values(test_case_5_input, test_case_5_mapping)
    assert actual_output_5 == expected_output_5, f"Test Case 5 Failed: Expected {expected_output_5}, Got {actual_output_5}"
    print("Test Case 5 Passed")