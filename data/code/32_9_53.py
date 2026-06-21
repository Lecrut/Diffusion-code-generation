class StringAnalyzer:
    def get_length(self, text):
        if not isinstance(text, str):
            raise ValueError('Input must be a string')
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text1 = "Hello, World!"
    sample_text2 = "Alibaba Cloud"
    print(analyzer.get_length(sample_text1))
    print(analyzer.get_length(sample_text2))