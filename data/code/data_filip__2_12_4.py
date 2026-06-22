class PalindromeChecker:
    ALNUM_FILTER = str.isalnum
    
    def __init__(self, text):
        self.text = text
    
    def check(self):
        cleaned = self._filter_and_normalize()
        return self._verify_sequence(cleaned)
    
    def _filter_and_normalize(self):
        result = []
        for char in self.text:
            if self.ALNUM_FILTER(char):
                result.append(char.lower())
        return result
    
    def _verify_sequence(self, seq):
        length = len(seq)
        for index in range(length // 2):
            if seq[index] != seq[length - 1 - index]:
                return False
        return True

if __name__ == '__main__':
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Was it a car or a cat I saw?",
        "No 'x' in Nixon",
        "12321"
    ]
    
    for case in test_cases:
        checker = PalindromeChecker(case)
        print(checker.check())