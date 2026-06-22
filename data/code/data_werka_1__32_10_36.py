class StringAnalyzer:
    MAX_LENGTH = 1000

    @staticmethod
    def is_within_max_length(text):
        return len(text) <= StringAnalyzer.MAX_LENGTH

    def get_length(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        if not StringAnalyzer.is_within_max_length(text):
            raise ValueError(f"Text length exceeds maximum allowed: {StringAnalyzer.MAX_LENGTH}")
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text = "Hello, World!"
    print(analyzer.get_length(sample_text))