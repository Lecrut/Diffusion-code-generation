import re

def is_palindrome(s):
    cleaned = re.sub('[^a-zA-Z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]
if __name__ == '__main__':
    sample_values = ['A man, a plan, a canal: Panama', 'race a car', 'No lemon, no melon', 'Was it a car or a cat I saw?', 'Not a palindrome']
    for value in sample_values:
        print(is_palindrome(value))