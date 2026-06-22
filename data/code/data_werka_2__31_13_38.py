import re

def is_palindrome(s):
    cleaned = ''.join(re.findall(r'[a-zA-Z0-9]', s)).lower()
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    test_cases = [
        "A man, a plan, a canal: Panama",
        "No lemon, no melon",
        "Was it a car or a cat I saw?",
        "Not a palindrome"
    ]
    for case in test_cases:
        print(f"'{case}' is a palindrome: {is_palindrome(case)}")