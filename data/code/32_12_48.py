class TextAnalyzer:
    def __init__(self, text):
        self.text = text

    def count_characters(self):
        return sum(1 for char in self.text)

if __name__ == '__main__':
    sample_texts = [
        "Hello, World!",
        "Python",
        "OpenAI",
        "",
        "1234567890"
    ]

    analyzers = [TextAnalyzer(text) for text in sample_texts]

    for analyzer in analyzers:
        print(analyzer.count_characters())