def is_palindrome_two_pointer(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def is_palindrome_slicing(s: str) -> bool:
    return s == s[::-1]

if __name__ == '__main__':
    sample_string = "racecar"
    print("Using two-pointer approach:", is_palindrome_two_pointer(sample_string))
    print("Using slicing approach:", is_palindrome_slicing(sample_string))