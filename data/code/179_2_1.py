class WordReverser:
    def reverse_sentence(self, sentence: str) -> str:
        words = sentence.split()
        words.reverse()
        return " ".join(words)
if __name__ == '__main__':
    reverser = WordReverser()
    sample_sentence = "Hello world this is a test"
    reversed_sentence = reverser.reverse_sentence(sample_sentence)
    print(reversed_sentence)