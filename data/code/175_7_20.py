class WordSeparator:
    @staticmethod
    def separate_words(sentence):
        tokens = sentence.split()
        return [token.strip() for token in tokens if token]

if __name__ == '__main__':
    separator = WordSeparator()
    sample_sentences = [
        "I don't know where we are",
        "She won't go if you don't like it",
        "It's a test, isn't it?",
        "We don't care about that."
    ]
    for sentence in sample_sentences:
        print(separator.separate_words(sentence))