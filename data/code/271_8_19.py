import re

def clean_string(s):
    return re.sub(r'[^a-zA-Z]', '', s).lower()

def is_palindrome(s):
    cleaned = clean_string(s)
    return cleaned == cleaned[::-1]

def filter_palindromes(strings):
    return [s for s in strings if is_palindrome(s)]

if __name__ == '__main__':
    sample_strings = ["Able, was I saw elba", "No 'x' in Nixon", "Hello, World!"]
    print(filter_palindromes(sample_strings))