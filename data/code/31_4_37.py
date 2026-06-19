import re

def check_palindrome_with_spaces(s):
    cleaned = re.sub('[\\W_]', '', s).lower()
    return cleaned == cleaned[::-1]
if __name__ == '__main__':
    sample_values = ['A man, a plan, a canal: Panama', 'No lemon, no melon', 'Hello, World!', 'Was it a car or a cat I saw?']
    for value in sample_values:
        result = check_palindrome_with_spaces(value)
        print(f"'{value}' is a palindrome: {result}")