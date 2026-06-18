import re

def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome ignoring spaces, punctuation, and case."""
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    samples = [
        "A man, a plan, a canal: Panama",
        "race car",
        "Hello, World!",
        "Was it a cat and I saw a bad rat?",
        "Not a palindrome"
    ]

    for sample in samples:
        result = is_palindrome(sample)
        print(f"'{sample}' -> {result}")