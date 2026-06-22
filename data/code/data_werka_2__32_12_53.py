class StringAnalyzer:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def validate_input(text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")

    def count_characters(self):
        return len(self.text)

if __name__ == '__main__':
    sample_texts = [
        "Hello, World!",
        "Python",
        "OpenAI",
        "",
        "1234567890"
    ]

    for text in sample_texts:
        analyzer = StringAnalyzer(text)
        print(analyzer.count_characters())