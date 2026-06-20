class PalindromeChecker:
    ALNUM_SET = set(
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    )

    def __init__(self, case_sensitive=False):
        self.case_sensitive = case_sensitive

    def normalize(self, raw_input):
        result = []
        for char in raw_input:
            if char in self.ALNUM_SET:
                if self.case_sensitive:
                    result.append(char)
                else:
                    result.append(char.lower())
        return "".join(result)

    def check(self, text):
        cleaned = self.normalize(text)
        if not cleaned:
            return True
        length = len(cleaned)
        mid_point = length // 2
        for index in range(mid_point):
            if cleaned[index] != cleaned[length - 1 - index]:
                return False
        return True

if __name__ == '__main__':
    validator = PalindromeChecker()
    test_cases = [
        "Madam",
        "Step on no pets",
        "Not a palindrome",
        "12321",
        "Was it a car or a cat I saw?",
        "Hello, World!"
    ]
    for sample in test_cases:
        result = validator.check(sample)
        print(result)