import string

def check_palindrome_with_spaces(s):
    cleaned = ''.join((char.lower() for char in s if char.isalnum()))
    return cleaned == cleaned[::-1]
if __name__ == '__main__':
    sample1 = 'A man, a plan, a canal: Panama'
    sample2 = 'No lemon, no melon'
    sample3 = 'Hello, World!'
    print(check_palindrome_with_spaces(sample1))
    print(check_palindrome_with_spaces(sample2))
    print(check_palindrome_with_spaces(sample3))