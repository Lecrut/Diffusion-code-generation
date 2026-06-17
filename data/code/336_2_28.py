class StringAnalyzer:
    def check_for_duplicates(self, text):
        return len(text) != len(set(text))
if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text = "hello"
    result = analyzer.check_for_duplicates(sample_text)
    print(result)