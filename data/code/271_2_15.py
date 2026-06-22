ALPHABETIC_CHARS = set('abcdefghijklmnopqrstuvwxyz')
IGNORED_CHARS = ''.join(set(printable) - ALPHABETIC_CHARS)

def clean_string(s):
    return ''.join(c.lower() for c in s if c.isalpha())

def is_palindrome(s):
    cleaned = clean_string(s)
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_palindrome("race a car"))