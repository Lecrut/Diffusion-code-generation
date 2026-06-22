def is_palindrome_two_pointer(s: str) -> bool:
    s = s.lower()
    char_map = {chr(i): True for i in range(97, 123)}
    left, right = (0, len(s) - 1)
    while left < right:
        if s[left] not in char_map:
            left += 1
        elif s[right] not in char_map:
            right -= 1
        else:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
    return True

def is_palindrome_slicing(s: str) -> bool:
    s = ''.join((c.lower() for c in s if c.isalnum()))
    return s == s[::-1]
if __name__ == '__main__':
    sample_string = 'A man, a plan, a canal, Panama'
    print('Using two-pointer approach:', is_palindrome_two_pointer(sample_string))
    print('Using string slicing approach:', is_palindrome_slicing(sample_string))