def calculate_length(input_string):
    return len(input_string)
if __name__ == '__main__':
    test_string_short = "hello"
    test_string_long = "a" * 1000000
    test_string_empty = ""
    result_short = calculate_length(test_string_short)
    result_long = calculate_length(test_string_long)
    result_empty = calculate_length(test_string_empty)
    print(f"Length of '{test_string_short}': {result_short}")
    print(f"Length of '{test_string_long}': {result_long}")
    print(f"Length of '{test_string_empty}': {result_empty}")