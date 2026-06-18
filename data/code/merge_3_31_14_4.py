import re

def is_palindrome(s: str) -> bool:
    """Check if string s reads same forwards/backwards ignoring spaces/punctuation."""
    clean = re.sub(r'[^\w]', '', s).lower()
    return clean == clean[::-1]

if __name__ == '__main__':
    samples = [
        "A man, a plan, a canal: Panama",
        "race car",
        "hello world"
    ]

    for sample in samples:
        result = is_palindrome(sample)
        print(f"{sample!r} -> {result}")