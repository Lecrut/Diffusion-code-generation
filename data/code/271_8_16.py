import re

def clean_string(s):
    return re.sub(r'[^a-zA-Z]', '', s).lower()

def is_palindrome(s):
    return s == s[::-1]

def filter_palindromes(strings):
    cleaned_strings = [clean_string(s) for s in strings]
    return [s for s, c_s in zip(strings, cleaned_strings) if is_palindrome(c_s)]

if __name__ == '__main__':
    sample_strings = ["A man, a plan, a canal: Panama", "Madam, in Eden, I'm Adam", "Hello, World!"]
    print(filter_palindromes(sample_strings))