def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome ignoring case, spaces, and punctuation."""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    samples = ["racecar", "A man, a plan, a canal: Panama!", "hello"]
    for sample in samples:
        print(f"'{sample}' is {'a' if is_palindrome(sample) else 'not'} a palindrome")