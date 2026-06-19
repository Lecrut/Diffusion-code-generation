import string

def check_palindrome_with_spaces(s):
    cleaned = ''.join((char.lower() for char in s if char.isalnum()))
    return cleaned == cleaned[::-1]
if __name__ == '__main__':
    sample_string = 'A man, a plan, a canal: Panama'
    result = check_palindrome_with_spaces(sample_string)
    print(result)