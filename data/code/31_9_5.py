import re

def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome, ignoring case, spaces, and punctuation."""
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    samples = ["A man, a plan, a canal: Panama", "racecar", "hello"]
    for sample in samples:
        print(f"'{sample}' is {'a palindrome' if is_palindrome(sample) else 'not a palindrome'}")