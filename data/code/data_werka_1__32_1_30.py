class StringAnalyzer:
    def get_length(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text_1 = "Hello World"
    sample_text_2 = ""
    sample_text_3 = "a"
    print(analyzer.get_length(sample_text_1))
    print(analyzer.get_length(sample_text_2))
    print(analyzer.get_length(sample_text_3))