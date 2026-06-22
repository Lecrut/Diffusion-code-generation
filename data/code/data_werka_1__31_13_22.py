import re

def is_palindrome(s: str) -> bool:
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    sample_values = [
        "A man, a plan, a canal, Panama",
        "No lemon, no melon",
        "Hello, World!",
        "Was it a car or a cat I saw?",
        "Not a palindrome"
    ]
    
    for value in sample_values:
        print(f"'{value}' is a palindrome: {is_palindrome(value)}")