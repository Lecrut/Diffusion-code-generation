class FirstWordExtractor:
    def __init__(self, sentences):
        self.sentences = sentences

    def extract(self):
        return [sentence.split()[0] for sentence in self.sentences]

if __name__ == '__main__':
    sample_sentences = [
        "Hello world",
        "Python programming is fun",
        "List comprehension in Python"
    ]
    extractor = FirstWordExtractor(sample_sentences)
    first_words = extractor.extract()
    print(first_words)