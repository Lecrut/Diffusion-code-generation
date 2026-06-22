import re

def is_palindrome(s: str) -> bool:
    normalized_str = re.sub('[^a-zA-Z0-9]', '', s).lower()
    return normalized_str == normalized_str[::-1]
if __name__ == '__main__':
    sample_values = ['A man, a plan, a canal: Panama', 'race a car', 'No lemon, no melon', '', 'Was it a car or a cat I saw?']
    for value in sample_values:
        print(is_palindrome(value))