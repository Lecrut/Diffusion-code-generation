import string

def check_palindrome_with_spaces(text):
    cleaned_text = ''.join((char.lower() for char in text if char.isalnum()))
    return cleaned_text == cleaned_text[::-1]
if __name__ == '__main__':
    sample_values = ['A man, a plan, a canal, Panama', 'No lemon, no melon', 'Hello, World!', 'Was it a car or a cat I saw?']
    for value in sample_values:
        result = check_palindrome_with_spaces(value)
        print(f"'{value}' is a palindrome: {result}")