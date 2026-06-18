import re

def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome, ignoring case, spaces, punctuation, and numbers."""
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to avoid any user input or external dependencies.
    test_cases = ["A man, a plan, a canal: Panama", "race car", "hello world", "Madam"]

    for text in test_cases:
        result = is_palindrome(text)
        status = "Yes" if result else "No"
        print(f'"{text}" -> Palindrome? {status}')