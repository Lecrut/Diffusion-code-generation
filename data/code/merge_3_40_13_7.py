def get_first_letter(s: str) -> str:
    """Returns the first letter of a string, returning an empty string if input is empty."""
    return s[0] if len(s) > 0 else ""

if __name__ == '__main__':
    test_cases = ["", "Hello World", "!@#$%", "a"]
    
    for text in test_cases:
        result = get_first_letter(text)
        print(f"Input: '{text}' -> Output: '{result}'")