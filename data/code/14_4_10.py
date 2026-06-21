def check_duplicate_chars(input_str):
    original_length = len(input_str)
    unique_chars_set = set(input_str)
    unique_length = len(unique_chars_set)
    return original_length != unique_length

if __name__ == '__main__':
    test_value = "success"
    print(check_duplicate_chars(test_value))