def is_palindrome_two_pointer(s):
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

def is_palindrome_slicing(s):
    s = ''.join(c for c in s.lower() if c.isalnum())
    return s == s[::-1]

if __name__ == '__main__':
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
        "No lemon, no melon"
    ]
    
    for case in test_cases:
        print(f"Two-pointer approach: {case} -> {is_palindrome_two_pointer(case)}")
        print(f"Slicing approach: {case} -> {is_palindrome_slicing(case)}")