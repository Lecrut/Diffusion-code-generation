import re

def is_palindrome(s):
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    test_strings = ["A man, a plan, a canal: Panama", "race a car", " ", "No lemon, no melon"]
    for test in test_strings:
        print(f"'{test}' is a palindrome: {is_palindrome(test)}")