class StringAnalyzer:
    def get_length(self, text):
        length = 0
        for char in text:
            length += 1
        return length

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text = "Hello, World!"
    print(analyzer.get_length(sample_text))