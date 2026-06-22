class StringAnalyzer:
    def get_length(self, text):
        self._validate_input(text)
        return len(text)

    def _validate_input(self, text):
        if not isinstance(text, str):
            raise ValueError('Input must be a string')

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text1 = "Hello, World!"
    sample_text2 = "Alibaba Cloud"
    try:
        print(analyzer.get_length(sample_text1))
        print(analyzer.get_length(12345))
    except ValueError as e:
        print(e)