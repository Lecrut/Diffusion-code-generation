class PalindromeChecker:
    LOWERCASE = True
    IGNORE_SPACES = True

    @staticmethod
    def clean(text):
        cleaned = ""
        for char in text:
            if PalindromeChecker.IGNORE_SPACES and char == " ":
                continue
            if PalindromeChecker.LOWERCASE:
                cleaned += char.lower()
            else:
                cleaned += char
        return cleaned

    @classmethod
    def is_palindrome(cls, text):
        cleaned = cls.clean(text)
        length = len(cleaned)
        half = length // 2
        for i in range(half):
            if cleaned[i] != cleaned[length - 1 - i]:
                return False
        return True

if __name__ == '__main__':
    samples = ["racecar", "hello", "A man a plan a canal Panama", "12321", "python"]
    for sample in samples:
        print(PalindromeChecker.is_palindrome(sample))