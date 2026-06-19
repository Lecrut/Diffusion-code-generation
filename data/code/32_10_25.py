class StringAnalyzer:
    DEFAULT_TEXT = "Hello, World!"
    
    def get_length(self, text=DEFAULT_TEXT):
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text = "This is a test string."
    print(analyzer.get_length(sample_text))