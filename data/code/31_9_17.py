def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome ignoring case and non-alphanumeric characters."""
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    samples = ["A man, a plan, a canal: Panama", "race car", "hello world"]