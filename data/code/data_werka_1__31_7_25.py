def is_palindrome(s):
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

if __name__ == '__main__':
    sample_values = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
        "No lemon, no melon"
    ]
    
    for value in sample_values:
        print(is_palindrome(value))