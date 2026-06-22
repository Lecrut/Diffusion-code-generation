def is_palindrome_two_pointer(s: str) -> bool:
    s = s.lower().replace(' ', '')
    left, right = (0, len(s) - 1)
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def is_palindrome_slicing(s: str) -> bool:
    s = s.lower().replace(' ', '')
    return s == s[::-1]
if __name__ == '__main__':
    sample_string_1 = 'A man a plan a canal Panama'
    sample_string_2 = 'racecar'
    sample_string_3 = 'hello world'
    print(is_palindrome_two_pointer(sample_string_1))
    print(is_palindrome_slicing(sample_string_1))
    print(is_palindrome_two_pointer(sample_string_2))
    print(is_palindrome_slicing(sample_string_2))
    print(is_palindrome_two_pointer(sample_string_3))
    print(is_palindrome_slicing(sample_string_3))