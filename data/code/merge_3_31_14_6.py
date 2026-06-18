import re

def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome ignoring spaces, punctuation, and case."""
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    samples = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Was it a cat and I saw a raccoon?",
        "",
        "No 'x' in Nixon"
    ]

    for sample in samples:
        result = is_palindrome(sample)
        print(f"'{sample}' -> {result}")