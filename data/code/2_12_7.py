ALPHANUMERIC_FILTER_METHOD = lambda c: c.isalnum()
CASE_NORMALIZATION_METHOD = lambda c: c.lower()

def is_palindrome(s):
    filtered_chars = []
    for char in s:
        if ALPHANUMERIC_FILTER_METHOD(char):
            filtered_chars.append(CASE_NORMALIZATION_METHOD(char))
    
    left = 0
    right = len(filtered_chars) - 1
    
    while left < right:
        if filtered_chars[left] != filtered_chars[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "No 'x' in Nixon",
        "12321",
        "12345",
        "Madam",
        "Not a palindrome"
    ]
    
    for case in test_cases:
        result = is_palindrome(case)
        print(f"{case}: {result}")