class StringAnalyzer:
    def get_length(self, text):
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text = "Hello, World!"
    length = analyzer.get_length(sample_text)
    print(length)