import string

def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

if __name__ == '__main__':
    sample_strings = ["A man, a plan, a canal: Panama", "racecar", "hello"]
    results = {s: is_palindrome(s) for s in sample_strings}
    print(results)