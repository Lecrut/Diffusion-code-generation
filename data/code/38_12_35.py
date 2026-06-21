class StringAnalyzer:
    IGNORE_CASE = True

    @staticmethod
    def normalize_string(s):
        if StringAnalyzer.IGNORE_CASE:
            return s.lower()
        return s

    def has_repeated_letters(self, text):
        normalized_text = StringAnalyzer.normalize_string(text)
        seen = set()
        for char in normalized_text:
            if char.isalpha() and char in seen:
                return True
            seen.add(char)
        return False

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_string1 = "hello world"
    sample_string2 = "Programming"
    sample_string3 = "abcdefg"
    sample_string4 = "aabbccddeeff"
    print(analyzer.has_repeated_letters(sample_string1))
    print(analyzer.has_repeated_letters(sample_string2))
    print(analyzer.has_repeated_letters(sample_string3))
    print(analyzer.has_repeated_letters(sample_string4))