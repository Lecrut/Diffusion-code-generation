class StringAnalyzer:

    def check_for_duplicates(self, text):
        if not isinstance(text, str):
            raise ValueError('Input must be a string')
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
    sample_string4 = 'aabbccddeeff'
    print(analyzer.check_for_duplicates(sample_string1))
    print(analyzer.check_for_duplicates(sample_string2))
    print(analyzer.check_for_duplicates(sample_string3))
    print(analyzer.check_for_duplicates(sample_string4))