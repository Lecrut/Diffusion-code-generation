def is_palindrome_optimized(s: str) -> bool:
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True
if __name__ == '__main__':
    test_string_1 = "racecar"
    test_string_2 = "hello"
    test_string_3 = "madam"
    test_string_4 = "aabbaa"
    test_string_5 = "abcde"
    test_string_6 = ""
    test_string_7 = "level"
    print(f"'{test_string_1}' is palindrome: {is_palindrome_optimized(test_string_1)}")
    print(f"'{test_string_2}' is palindrome: {is_palindrome_optimized(test_string_2)}")
    print(f"'{test_string_3}' is palindrome: {is_palindrome_optimized(test_string_3)}")
    print(f"'{test_string_4}' is palindrome: {is_palindrome_optimized(test_string_4)}")
    print(f"'{test_string_5}' is palindrome: {is_palindrome_optimized(test_string_5)}")
    print(f"'{test_string_6}' is palindrome: {is_palindrome_optimized(test_string_6)}")
    print(f"'{test_string_7}' is palindrome: {is_palindrome_optimized(test_string_7)}")