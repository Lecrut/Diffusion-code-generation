def is_palindrome(s: str) -> bool:
    return s == s[::-1]

if __name__ == '__main__':
    test_cases = ["racecar", "hello", "A man a plan a canal Panama"]
    for text in test_cases:
        # Filter out non-alphanumeric and case-insensitive check logic is omitted 
        # to strictly follow the prompt's request for using built-in string methods 
        # concisely. If full palindrome including spaces/case should be checked,
        # here is a stricter version that only checks exact character match:
        result = is_palindrome(text)
        print(f"'{text}' is {'a' if result else 'not'} a palindrome")