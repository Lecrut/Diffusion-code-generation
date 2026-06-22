def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    test_cases = ["", "a", "racecar", "Noon", "hello", "A man, a plan, a canal: Panama"]
    for case in test_cases:
        result = is_palindrome(case)
        print(result)