def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome using built-in methods."""
    clean = "".join(ch.lower() for ch in s if ch.isalnum())
    return clean == clean[::-1]

if __name__ == '__main__':
    samples = ["racecar", "Python 3.5", "Hello, World!", "not a palindrome"]
    print(is_palindrome("racecar"))          # True
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome("No 'x' in Nixon"))   # False