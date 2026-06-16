def calculate_length(input_string):
    return len(input_string)
if __name__ == '__main__':
    test_string_short = "hello"
    test_string_long = "a" * 1000000
    test_string_empty = ""
    print(f"Length of '{test_string_short}': {calculate_length(test_string_short)}")
    print(f"Length of '{test_string_long}': {calculate_length(test_string_long)}")
    print(f"Length of '{test_string_empty}': {calculate_length(test_string_empty)}")