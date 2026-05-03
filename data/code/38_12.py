class StringAnalyzer:
    def check_for_duplicates(self, text):
        seen = set()
        duplicates = set()
        for char in text:
            if char in seen:
                duplicates.add(char)
            seen.add(char)
        return sorted(list(duplicates))
if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_string1 = "hello world"
    sample_string2 = "programming"
    sample_string3 = "abcdefg"
    sample_string4 = "aabbccddeeff"
    print(f"'{sample_string1}': {analyzer.check_for_duplicates(sample_string1)}")
    print(f"'{sample_string2}': {analyzer.check_for_duplicates(sample_string2)}")
    print(f"'{sample_string3}': {analyzer.check_for_duplicates(sample_string3)}")
    print(f"'{sample_string4}': {analyzer.check_for_duplicates(sample_string4)}")