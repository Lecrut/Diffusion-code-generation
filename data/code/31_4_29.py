import string

def check_palindrome_with_spaces(s):
    cleaned = ''.join((char.lower() for char in s if char.isalnum()))
    return cleaned == cleaned[::-1]
if __name__ == '__main__':
    sample_values = ['A man, a plan, a canal: Panama', 'race a car', 'No lemon, no melon', 'Was it a car or a cat I saw?', 'Not a palindrome']
    for value in sample_values:
        result = check_palindrome_with_spaces(value)
        print(f"'{value}' is a palindrome: {result}")