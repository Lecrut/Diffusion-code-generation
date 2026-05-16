def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
if __name__ == '__main__':
    test_string1 = "racecar"
    test_string2 = "hello"
    test_string3 = "madam"
    result1 = is_palindrome(test_string1)
    print(f"Input: {test_string1}")
    print(f"Is palindrome: {result1}")
    result2 = is_palindrome(test_string2)
    print(f"Input: {test_string2}")
    print(f"Is palindrome: {result2}")
    result3 = is_palindrome(test_string3)
    print(f"Input: {test_string3}")
    print(f"Is palindrome: {result3}")