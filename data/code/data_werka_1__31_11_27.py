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
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

if __name__ == '__main__':
    sample_values = ["A man, a plan, a canal: Panama", "race a car", " ", "No lemon, no melon"]
    
    print("Using two-pointer approach:")
    for value in sample_values:
        print(f"'{value}' -> {is_palindrome_two_pointer(value)}")
    
    print("\nUsing string slicing approach:")
    for value in sample_values:
        print(f"'{value}' -> {is_palindrome_slicing(value)}")