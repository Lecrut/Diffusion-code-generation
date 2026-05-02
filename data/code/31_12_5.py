import time
def is_palindrome_two_pointers(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
def is_palindrome_slicing(s: str) -> bool:
    return s == s[::-1]
if __name__ == '__main__':
    test_string_1 = "racecar"
    test_string_2 = "hello"
    test_string_3 = "madam"
    test_string_4 = "aabbaa"
    test_string_5 = ""
    test_string_6 = "level"
    print(f"Testing '{test_string_1}':")
    print(f"Two Pointers: {is_palindrome_two_pointers(test_string_1)}")
    print(f"Slicing: {is_palindrome_slicing(test_string_1)}")
    print("-" * 20)
    print(f"Testing '{test_string_2}':")
    print(f"Two Pointers: {is_palindrome_two_pointers(test_string_2)}")
    print(f"Slicing: {is_palindrome_slicing(test_string_2)}")
    print("-" * 20)
    print(f"Testing '{test_string_3}':")
    print(f"Two Pointers: {is_palindrome_two_pointers(test_string_3)}")
    print(f"Slicing: {is_palindrome_slicing(test_string_3)}")
    print("-" * 20)
    print(f"Testing '{test_string_4}':")
    print(f"Two Pointers: {is_palindrome_two_pointers(test_string_4)}")
    print(f"Slicing: {is_palindrome_slicing(test_string_4)}")
    print("-" * 20)
    print(f"Testing '{test_string_5}':")
    print(f"Two Pointers: {is_palindrome_two_pointers(test_string_5)}")
    print(f"Slicing: {is_palindrome_slicing(test_string_5)}")
    print("-" * 20)
    print(f"Testing '{test_string_6}':")
    print(f"Two Pointers: {is_palindrome_two_pointers(test_string_6)}")
    print(f"Slicing: {is_palindrome_slicing(test_string_6)}")
    print("-" * 20)