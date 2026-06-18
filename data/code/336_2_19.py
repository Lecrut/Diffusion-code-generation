class StringAnalyzer:
    def check_for_duplicates(self, text):
        return len(set(text)) != len(text)
if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text_1 = "hello"
    sample_text_2 = "abcdefg"
    result_1 = analyzer.check_for_duplicates(sample_text_1)
    result_2 = analyzer.check_for_duplicates(sample_text_2)
    print(f"'{sample_text_1}' has duplicates: {result_1}")
    print(f"'{sample_text_2}' has duplicates: {result_2}")