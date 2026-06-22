import re

ALNUM_PATTERN = re.compile(r'[^a-z0-9]')

def normalize(text):
    return ALNUM_PATTERN.sub('', text.lower())

def is_palindrome(text):
    cleaned = normalize(text)
    if len(cleaned) == 0:
        return True
    left = 0
    right = len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

class PalindromeChecker:
    def __init__(self, value):
        self.value = value

    def check(self):
        return is_palindrome(self.value)

if __name__ == '__main__':
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "No 'x' in Nixon",
        "Was it a car or a cat I saw?",
        "12321",
        "Not a palindrome",
        "",
        "a"
    ]

    for case in test_cases:
        checker = PalindromeChecker(case)
        result = checker.check()
        print(f"{case} -> {result}")