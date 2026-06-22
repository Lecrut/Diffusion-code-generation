class PalindromeChecker:
    def __init__(self, text: str):
        self.text = text

    def reverse(self) -> str:
        return self.text[::-1]

    def is_palindrome(self) -> bool:
        return self.text == self.reverse()

if __name__ == '__main__':
    test_cases = ["radar", "hello", "noon", "Python", "civic"]
    
    for sample in test_cases:
        checker = PalindromeChecker(sample)
        result = checker.is_palindrome()
        print(result)