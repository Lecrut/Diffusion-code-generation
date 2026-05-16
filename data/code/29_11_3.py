def reverse_word(s):
    return s[::-1]
if __name__ == '__main__':
    test_string1 = "hello"
    result1 = reverse_word(test_string1)
    print(f"Input: {test_string1}, Output: {result1}")
    test_string2 = "world"
    result2 = reverse_word(test_string2)
    print(f"Input: {test_string2}, Output: {result2}")
    test_string3 = "Python"
    result3 = reverse_word(test_string3)
    print(f"Input: {test_string3}, Output: {result3}")