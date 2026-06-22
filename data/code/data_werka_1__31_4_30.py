import re

def check_palindrome_with_spaces(s):
    cleaned = re.sub('[\\W_]+', '', s).lower()
    return cleaned == cleaned[::-1]
if __name__ == '__main__':
    sample_string = 'A man, a plan, a canal: Panama'
    result = check_palindrome_with_spaces(sample_string)
    print(result)