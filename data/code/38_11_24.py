class StringAnalyzer:

    @staticmethod
    def _is_letter(char):
        return 'a' <= char <= 'z' or 'A' <= char <= 'Z'

    @staticmethod
    def _normalize_char(char):
        return char.lower()

    def check_for_duplicates(self, text):
        letter_counts = {}
        for char in text:
            if self._is_letter(char):
                normalized_char = self._normalize_char(char)
                letter_counts[normalized_char] = letter_counts.get(normalized_char, 0) + 1
        repeated_letters = {letter for letter, count in letter_counts.items() if count > 1}
        return repeated_letters
if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample1 = 'hello world'
    sample2 = 'programming'
    sample3 = 'aabbccddeeffg'
    sample4 = 'abcde'
    print(analyzer.check_for_duplicates(sample1))
    print(analyzer.check_for_duplicates(sample2))
    print(analyzer.check_for_duplicates(sample3))
    print(analyzer.check_for_duplicates(sample4))