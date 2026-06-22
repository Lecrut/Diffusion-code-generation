class SentenceProcessor:
    @staticmethod
    def extract_first_word(sentence):
        parts = sentence.split()
        return parts[0] if parts else None

    def get_first_words(self, sentences):
        return [self.extract_first_word(sentence) for sentence in sentences]

if __name__ == '__main__':
    sample_sentences = [
        "Hello world",
        "Python programming is fun",
        "List comprehension in Python"
    ]
    processor = SentenceProcessor()
    first_words = processor.get_first_words(sample_sentences)
    print(first_words)