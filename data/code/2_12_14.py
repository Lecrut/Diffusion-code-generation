def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    test_cases = ["A man, a plan, a canal: Panama", "race a car", "No 'x' in Nixon", "Was it a car or a cat I saw?", "Hello"]
    for case in test_cases:
        print(is_palindrome(case))