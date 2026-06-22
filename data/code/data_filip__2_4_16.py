def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    test_cases = ["", "a", "A man, a plan, a canal: Panama", "hello", "Was it a car or a cat I saw?"]
    for case in test_cases:
        print(is_palindrome(case))