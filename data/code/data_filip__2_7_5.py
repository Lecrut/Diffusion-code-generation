def is_palindrome(s):
    return all(a == b for a, b in zip(s, reversed(s)))

if __name__ == '__main__':
    test_value = "racecar"
    result = is_palindrome(test_value)
    print(result)
    test_value_2 = "hello"
    result_2 = is_palindrome(test_value_2)
    print(result_2)