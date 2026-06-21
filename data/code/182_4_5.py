def extract_chars(s):
    return tuple(s)

if __name__ == '__main__':
    test_string_1 = "hello"
    result_1 = extract_chars(test_string_1)
    print(f"Input: '{test_string_1}', Output: {result_1}")
    test_string_2 = ""
    result_2 = extract_chars(test_string_2)
    print(f"Input: '{test_string_2}', Output: {result_2}")
    test_string_3 = "Python"
    result_3 = extract_chars(test_string_3)
    print(f"Input: '{test_string_3}', Output: {result_3}")
    test_string_4 = "a"
    result_4 = extract_chars(test_string_4)
    print(f"Input: '{test_string_4}', Output: {result_4}")