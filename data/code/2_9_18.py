class PalindromeChecker:
    def __init__(self):
        self.cache = {}

    def check(self, text):
        if text in self.cache:
            return self.cache[text]
        normalized = ''.join(c.lower() for c in text if c.isalnum())
        result = normalized == normalized[::-1]
        self.cache[text] = result
        return result

if __name__ == '__main__':
    checker = PalindromeChecker()
    print(checker.check("racecar"))
    print(checker.check("Was it a car or a cat I saw?"))
    print(checker.check("Python"))
    print(checker.check("No 'x' in Nixon"))