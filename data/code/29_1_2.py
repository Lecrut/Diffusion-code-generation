import time
def reverse_word(s):
    return s[::-1]
if __name__ == '__main__':
    test_string_1 = "hello"
    result_1 = reverse_word(test_string_1)
    print(f"Input: {test_string_1}, Output: {result_1}")
    test_string_2 = "Python"
    result_2 = reverse_word(test_string_2)
    print(f"Input: {test_string_2}, Output: {result_2}")
    test_string_3 = "racecar"
    result_3 = reverse_word(test_string_3)
    print(f"Input: {test_string_3}, Output: {result_3}")