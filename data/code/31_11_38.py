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
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

if __name__ == '__main__':
    test_strings = ["A man, a plan, a canal: Panama", "racecar", "hello", "Was it a car or a cat I saw?"]
    results_two_pointer = [is_palindrome_two_pointer(s) for s in test_strings]
    results_slicing = [is_palindrome_slicing(s) for s in test_strings]
    
    print("Two-pointer approach results:", results_two_pointer)
    print("Slicing approach results:", results_slicing)