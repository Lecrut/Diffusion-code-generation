import string

def check_palindrome_with_spaces(text):
    cleaned_text = ''.join((char.lower() for char in text if char.isalnum()))
    return cleaned_text == cleaned_text[::-1]
if __name__ == '__main__':
    sample_text = 'A man, a plan, a canal: Panama'
    result = check_palindrome_with_spaces(sample_text)
    print(result)