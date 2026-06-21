def is_palindrome_two_pointer(s: str) -> bool:
    s = s.lower()
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        else:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
    return True

def is_palindrome_slicing(s: str) -> bool:
    filtered_chars = ''.join(c.lower() for c in s if c.isalnum())
    return filtered_chars == filtered_chars[::-1]

if __name__ == '__main__':
    sample_string1 = "A man, a plan, a canal, Panama"
    sample_string2 = "racecar"
    sample_string3 = "hello"

    print("Using two-pointer approach for 'A man, a plan, a canal, Panama':", is_palindrome_two_pointer(sample_string1))
    print("Using slicing approach for 'A man, a plan, a canal, Panama':", is_palindrome_slicing(sample_string1))

    print("Using two-pointer approach for 'racecar':", is_palindrome_two_pointer(sample_string2))
    print("Using slicing approach for 'racecar':", is_palindrome_slicing(sample_string2))

    print("Using two-pointer approach for 'hello':", is_palindrome_two_pointer(sample_string3))
    print("Using slicing approach for 'hello':", is_palindrome_slicing(sample_string3))