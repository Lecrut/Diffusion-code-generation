class StringOperations:
    @classmethod
    def is_palindrome(cls, s: str) -> bool:
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]

if __name__ == '__main__':
    test_cases = [
        "A man, a plan, a canal, Panama",
        "racecar",
        "hello",
        "No lemon, no melon"
    ]
    
    for case in test_cases:
        result = StringOperations.is_palindrome(case)
        print(f"'{case}' is a palindrome: {result}")