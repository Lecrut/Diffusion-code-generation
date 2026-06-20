class PalindromeChecker:
    @staticmethod
    def is_palindrome(s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

if __name__ == '__main__':
    sample_values = [
        "racecar",
        "hello",
        "A man a plan a canal Panama",
        "Was it a car or a cat I saw"
    ]
    
    for value in sample_values:
        print(f"'{value}' is palindrome: {PalindromeChecker.is_palindrome(value)}")