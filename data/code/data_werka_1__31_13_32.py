def is_palindrome(text):
    processed_text = ''.join(filter(str.isalnum, text)).lower()
    return processed_text == processed_text[::-1]

if __name__ == '__main__':
    test_cases = [
        ("racecar", True),
        ("hello", False),
        ("", True),
        ("Madam", True),
        ("A man, a plan, a canal: Panama", True),
        ("No lemon, no melon", True),
        ("12321", True),
        ("abcde", False),
        ("level", True)
    ]
    
    for text, expected in test_cases:
        result = is_palindrome(text)
        print(f"'{text}' -> {result} (expected: {expected})")