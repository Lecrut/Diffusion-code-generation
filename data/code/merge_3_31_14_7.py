import re

def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome ignoring spaces, punctuation, and case."""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    samples = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Was it a car or a cat I saw?",
        "",
        "No 'x' in Nixon"
    ]

    for sample in samples:
        result = is_palindrome(sample)
        print(f"'{sample}' -> {result}")