import re

def is_palindrome(input_text):
    alphanumeric_only = re.sub(r'[^a-zA-Z0-9]', '', input_text)
    normalized = alphanumeric_only.lower()
    reversed_text = normalized[::-1]
    return normalized == reversed_text

class PalindromeChecker:
    def __init__(self, text):
        self.text = text
    
    def check(self):
        return is_palindrome(self.text)

if __name__ == '__main__':
    test_cases = [
        "A man, a plan, a canal: Panama",
        "No 'x' in Nixon",
        "Hello, World!",
        "Step on no pets",
        "12321",
        "12345"
    ]
    
    for case in test_cases:
        result = is_palindrome(case)
        print(f"Input: '{case}' -> Result: {result}")
    
    checker_instance = PalindromeChecker("Madam")
    print(f"Class check: {checker_instance.check()}")