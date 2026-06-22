def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

if __name__ == '__main__':
    sample_values = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "No 'x' in Nixon",
        "Was it a car or a cat I saw?",
        "Not a palindrome"
    ]
    
    for value in sample_values:
        print(is_palindrome(value))