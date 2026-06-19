import string

def check_palindrome_with_spaces(s):
    cleaned = ''.join((c.lower() for c in s if c.isalnum()))
    return cleaned == cleaned[::-1]
if __name__ == '__main__':
    sample_string = 'A man, a plan, a canal: Panama'
    print(check_palindrome_with_spaces(sample_string))