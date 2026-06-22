import re

ALNUM_PATTERN = re.compile(r'[^a-z0-9]')

def normalize_text(text: str) -> str:
    lower_text = text.lower()
    return ALNUM_PATTERN.sub('', lower_text)

def check_palindrome(input_string: str) -> bool:
    normalized = normalize_text(input_string)
    reversed_text = normalized[::-1]
    return normalized == reversed_text

class PalindromeChecker:
    def __init__(self, text: str):
        self.original_text = text
    
    def is_palindrome(self) -> bool:
        normalized = normalize_text(self.original_text)
        return normalized == normalized[::-1]

if __name__ == '__main__':
    test_cases = [
        "Madam, I'm Adam",
        "12321",
        "No lemon, no melon",
        "Not a palindrome"
    ]
    
    for case in test_cases:
        result = check_palindrome(case)
        print(result)
    
    checker_instance = PalindromeChecker("A Toyota!")
    print(checker_instance.is_palindrome())