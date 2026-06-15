class WordReverser:
    def reverse_sentence(self, sentence):
        words = sentence.split()
        reversed_words = words[::-1]
        reversed_sentence = " ".join(reversed_words)
        return reversed_sentence
if __name__ == '__main__':
    reverser = WordReverser()
    sample_sentence = "This is a sample sentence"
    reversed_sentence = reverser.reverse_sentence(sample_sentence)
    print(reversed_sentence)