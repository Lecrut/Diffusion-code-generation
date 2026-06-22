class StringAnalyzer:

    def has_repeated_letters(self, text):
        seen = set()
        for char in text:
            if char in seen:
                return True
            seen.add(char)
        return False
if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_string1 = 'hello world'
    sample_string2 = 'programming'
    sample_string3 = 'abcdefg'
    print(analyzer.has_repeated_letters(sample_string1))
    print(analyzer.has_repeated_letters(sample_string2))
    print(analyzer.has_repeated_letters(sample_string3))