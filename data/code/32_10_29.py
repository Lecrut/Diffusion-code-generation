class StringAnalyzer:
    def get_length(self, text):
        return len(text)

if __name__ == '__main__':
    SAMPLE_TEXT = "Hello, World!"
    analyzer = StringAnalyzer()
    length_of_sample_text = analyzer.get_length(SAMPLE_TEXT)
    print(length_of_sample_text)