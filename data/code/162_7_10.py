def name_length_mapping(user_names):
    return {name: len(name) for name in user_names}

if __name__ == '__main__':
    sample_user_names = ["Alice", "Bob", "Charlie"]
    expected_output = {"Alice": 5, "Bob": 3, "Charlie": 7}
    actual_output = name_length_mapping(sample_user_names)
    assert actual_output == expected_output, f"Test Case Failed: Expected {expected_output}, Got {actual_output}"
    print(actual_output)