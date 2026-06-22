class StringAnalyzer:
    MAX_LENGTH = 1000

    @staticmethod
    def _validate_length(length):
        if length > StringAnalyzer.MAX_LENGTH:
            raise ValueError("String length exceeds the maximum allowed length.")

    def get_length(self, text):
        length = len(text)
        StringAnalyzer._validate_length(length)
        return length

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text = "Hello, World!"
    print(analyzer.get_length(sample_text))