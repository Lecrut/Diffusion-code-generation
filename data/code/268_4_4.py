class SentenceProcessor:
    def __init__(self, sentences):
        self.sentences = sentences

    def get_first_words(self):
        return [sentence.split()[0] for sentence in self.sentences]

if __name__ == '__main__':
    sample_sentences = [
        "Hello world",
        "Python programming is fun",
        "List comprehension in Python"
    ]
    processor = SentenceProcessor(sample_sentences)
    first_words = processor.get_first_words()
    print(first_words)