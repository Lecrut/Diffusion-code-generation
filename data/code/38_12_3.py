class StringAnalyzer:
    def check_for_duplicates(self, text):
        seen = set()
        duplicates = set()
        for char in text:
            if char in seen:
                duplicates.add(char)
            else:
                seen.add(char)
        return sorted(list(duplicates))
if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_string_1 = "hello world"
    sample_string_2 = "programming"
    sample_string_3 = "abcdefg"
    sample_string_4 = "aabbccddeeff"
    sample_string_5 = "mississippi"
    print(f"'{sample_string_1}': {analyzer.check_for_duplicates(sample_string_1)}")
    print(f"'{sample_string_2}': {analyzer.check_for_duplicates(sample_string_2)}")
    print(f"'{sample_string_3}': {analyzer.check_for_duplicates(sample_string_3)}")
    print(f"'{sample_string_4}': {analyzer.check_for_duplicates(sample_string_4)}")
    print(f"'{sample_string_5}': {analyzer.check_for_duplicates(sample_string_5)}")