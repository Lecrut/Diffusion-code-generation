class StringAnalyzer:
    def check_for_duplicates(self, text):
        seen = set()
        for char in text:
            if char in seen:
                return True
            seen.add(char)
        return False
if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text_1 = "hello"
    result_1 = analyzer.check_for_duplicates(sample_text_1)
    print(f"'{sample_text_1}' has duplicates: {result_1}")
    sample_text_2 = "abcdefg"
    result_2 = analyzer.check_for_duplicates(sample_text_2)
    print(f"'{sample_text_2}' has duplicates: {result_2}")