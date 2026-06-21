class TextProcessor:
    def __init__(self, text):
        self.text = text

    def extract_words(self):
        return [word for word in self.text.split() if word]

if __name__ == '__main__':
    processor1 = TextProcessor("Hello world! This is a test, with various spaces and punctuation.")
    processor2 = TextProcessor("  \tWord1... Word2? End.")
    processor3 = TextProcessor("OnlyWords")

    print(processor1.extract_words())
    print(processor2.extract_words())
    print(processor3.extract_words())