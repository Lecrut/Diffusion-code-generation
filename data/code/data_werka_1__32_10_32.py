class StringAnalyzer:
    MAX_LENGTH = 1000

    @staticmethod
    def is_within_max_length(text):
        return len(text) <= StringAnalyzer.MAX_LENGTH

    def get_length(self, text):
        if not StringAnalyzer.is_within_max_length(text):
            raise ValueError("Text exceeds maximum allowed length.")
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text = "Hello World! This is a test."
    print(analyzer.get_length(sample_text))