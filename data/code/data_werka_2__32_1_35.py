class StringAnalyzer:
    def get_length(self, text):
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    SAMPLE_TEXT = "Hello, World!"
    length_of_text = analyzer.get_length(SAMPLE_TEXT)
    print(length_of_text)