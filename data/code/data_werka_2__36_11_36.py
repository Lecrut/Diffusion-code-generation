class SentenceReverser:
    def __init__(self, sentence):
        if not isinstance(sentence, str):
            raise ValueError("Input must be a string")
        self.sentence = sentence

    def reverse_words(self):
        words = self.sentence.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Hello world this is a test"
    reverser = SentenceReverser(sample_sentence)
    reversed_sentence = reverser.reverse_words()
    print(reversed_sentence)