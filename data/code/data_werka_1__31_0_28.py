import re

def is_palindrome(s):
    cleaned = re.sub('[^a-zA-Z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]
if __name__ == '__main__':
    test_cases = ['A man, a plan, a canal: Panama', 'race a car', ' ', 'No lemon, no melon']
    for case in test_cases:
        print(is_palindrome(case))