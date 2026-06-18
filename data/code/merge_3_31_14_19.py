import re

def is_palindrome(s: str) -> bool:
    """Check if a string reads the same forwards and backward, ignoring spaces and punctuation."""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    samples = [
        "A man, a plan, a canal: Panama",
        "racecar",
        "No 'x' niixon",
        "Hello, World!",
        "",
        "Was it a car or a cat I saw?",
    ]

    for sample in samples:
        result = is_palindrome(sample)
        print(f"'{sample}' -> {result}")