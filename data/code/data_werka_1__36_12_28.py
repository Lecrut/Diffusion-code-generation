class WordReverser:
    def __init__(self):
        self.separator = ' '

    def reverse_words(self, sentence):
        words = sentence.split(self.separator)
        reversed_sentence = self.separator.join(words[::-1])
        return reversed_sentence

if __name__ == '__main__':
    reverser = WordReverser()
    sample_sentence1 = "Hello world this is a test"
    reversed_sentence1 = reverser.reverse_words(sample_sentence1)
    print(f"Original: {sample_sentence1}, Reversed: {reversed_sentence1}")

    sample_sentence2 = "Python is fun and educational"
    reversed_sentence2 = reverser.reverse_words(sample_sentence2)
    print(f"Original: {sample_sentence2}, Reversed: {reversed_sentence2}")

    sample_sentence3 = "OpenAI GPT-4 is powerful"
    reversed_sentence3 = reverser.reverse_words(sample_sentence3)
    print(f"Original: {sample_sentence3}, Reversed: {reversed_sentence3}")