import re

def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome, ignoring spaces and punctuation."""
    cleaned = re.sub(r'[^\w]', '', s).lower()
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    samples = [
        "A man, a plan, a canal: Panama",
        "racecar",
        "Not a palindrome!",
        "",
        "Was it a car or a cat I saw?",
    ]

    for sample in samples:
        result = is_palindrome(sample)
        print(f"'{sample}' -> {result}")