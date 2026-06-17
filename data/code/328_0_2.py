def find_string_length(input_string):
    return len(input_string)
if __name__ == '__main__':
    test_string_1 = "hello"
    result_1 = find_string_length(test_string_1)
    print(f"The length of '{test_string_1}' is: {result_1}")
    test_string_2 = "Python"
    result_2 = find_string_length(test_string_2)
    print(f"The length of '{test_string_2}' is: {result_2}")
    test_string_3 = ""
    result_3 = find_string_length(test_string_3)
    print(f"The length of '{test_string_3}' is: {result_3}")