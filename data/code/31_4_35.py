import string

def check_palindrome_with_spaces(s):
    cleaned = ''.join((c.lower() for c in s if c.isalnum()))
    return cleaned == cleaned[::-1]
if __name__ == '__main__':
    sample_input = 'A man, a plan, a canal: Panama'
    result = check_palindrome_with_spaces(sample_input)
    print(result)