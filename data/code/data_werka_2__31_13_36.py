import string

def is_palindrome(s: str) -> bool:
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

if __name__ == '__main__':
    sample_values = [
        "A man, a plan, a canal, Panama",
        "No lemon, no melon",
        "Hello, World!",
        "Was it a car or a cat I saw?"
    ]
    
    for value in sample_values:
        print(f"'{value}' is a palindrome: {is_palindrome(value)}")