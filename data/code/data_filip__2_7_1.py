def is_palindrome_symmetric(s):
    return all(a == b for a, b in zip(s, reversed(s)))

if __name__ == '__main__':
    test_string_1 = "racecar"
    test_string_2 = "hello"
    result_1 = is_palindrome_symmetric(test_string_1)
    result_2 = is_palindrome_symmetric(test_string_2)
    print(result_1)
    print(result_2)