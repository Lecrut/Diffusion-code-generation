def is_palindrome_two_pointers(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
def is_palindrome_slicing(s):
    return s == s[::-1]
if __name__ == '__main__':
    test_string_1 = "racecar"
    test_string_2 = "hello"
    test_string_3 = "madam"
    test_string_4 = "aabbaa"
    test_string_5 = ""
    test_string_6 = "level"
    print(f"'{test_string_1}' - Two Pointers: {is_palindrome_two_pointers(test_string_1)}, Slicing: {is_palindrome_slicing(test_string_1)}")
    print(f"'{test_string_2}' - Two Pointers: {is_palindrome_two_pointers(test_string_2)}, Slicing: {is_palindrome_slicing(test_string_2)}")
    print(f"'{test_string_3}' - Two Pointers: {is_palindrome_two_pointers(test_string_3)}, Slicing: {is_palindrome_slicing(test_string_3)}")
    print(f"'{test_string_4}' - Two Pointers: {is_palindrome_two_pointers(test_string_4)}, Slicing: {is_palindrome_slicing(test_string_4)}")
    print(f"'{test_string_5}' - Two Pointers: {is_palindrome_two_pointers(test_string_5)}, Slicing: {is_palindrome_slicing(test_string_5)}")
    print(f"'{test_string_6}' - Two Pointers: {is_palindrome_two_pointers(test_string_6)}, Slicing: {is_palindrome_slicing(test_string_6)}")