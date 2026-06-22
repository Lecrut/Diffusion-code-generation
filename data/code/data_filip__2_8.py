def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    test_strings = ["A man, a plan, a canal: Panama", "race a car", "No 'x' in Nixon"]
    for text in test_strings:
        result = is_palindrome(text)
        print(result)