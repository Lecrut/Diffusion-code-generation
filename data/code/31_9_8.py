def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome, ignoring case and non-alphanumeric characters."""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    samples = ["A man, a plan", "race car", "hello world"]
    # Using the provided sample values directly without user input or arguments.
    print(any(is_palindrome(sample) for sample in samples))  # Outputs True if any are palindromes (e.g., 'race car')