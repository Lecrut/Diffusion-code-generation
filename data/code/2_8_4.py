class PalindromeChecker:
    def __init__(self, text):
        self.text = text

    def normalize(self):
        result = []
        for char in self.text:
            if char.isalnum():
                result.append(char.lower())
        return "".join(result)

    def check(self):
        normalized = self.normalize()
        length = len(normalized)
        mid = length // 2
        for i in range(mid):
            if normalized[i] != normalized[length - 1 - i]:
                return False
        return True

if __name__ == '__main__':
    samples = [
        "No lemon, no melon",
        "Not a palindrome",
        "Was it a car or a cat I saw?"
    ]
    for s in samples:
        checker = PalindromeChecker(s)
        print(checker.check())