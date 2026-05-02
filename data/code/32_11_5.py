def calculate_phrase_length(phrase: str) -> int:
    return len(phrase)
if __name__ == '__main__':
    test_string_1 = "hello world"
    result_1 = calculate_phrase_length(test_string_1)
    print(f"Length of '{test_string_1}': {result_1}")
    test_string_2 = ""
    result_2 = calculate_phrase_length(test_string_2)
    print(f"Length of '{test_string_2}': {result_2}")
    test_string_3 = "Python"
    result_3 = calculate_phrase_length(test_string_3)
    print(f"Length of '{test_string_3}': {result_3}")
    test_string_4 = "a" * 1000000
    result_4 = calculate_phrase_length(test_string_4)
    print(f"Length of long string: {result_4}")