def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome using built-in methods."""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    samples = ["racecar", "Hello, World!", "Python3.9"]
    for sample in samples:
        print(f"'{sample}' is a palindrome: {is_palindrome(sample)}")