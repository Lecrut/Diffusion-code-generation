import re

def is_palindrome(s):
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    sample_values = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "No lemon, no melon"
    ]
    
    for value in sample_values:
        print(f"'{value}' is a palindrome: {is_palindrome(value)}")