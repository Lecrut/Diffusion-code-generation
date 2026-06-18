import re

def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome, ignoring non-alphanumeric characters and case."""
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    # Sample test cases as hard-coded values to ensure the script runs without user input.
    sample_inputs = [
        "A man, a plan, a canal: Panama",
        "No 'x' in Nixon",
        "hello world"
    ]

    for text in sample_inputs:
        result = is_palindrome(text)
        if result:
            print(f"The string '{text}' IS a palindrome.")
        else:
            print(f"The string '{text}' is NOT a palindrome.")