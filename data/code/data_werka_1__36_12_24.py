class WordReverser:
    def reverse_words(self, sentence):
        words = sentence.split()
        reversed_sentence = ' '.join(words[::-1])
        return reversed_sentence

if __name__ == '__main__':
    reverser = WordReverser()
    sample_sentence1 = "The quick brown fox"
    reversed_sentence1 = reverser.reverse_words(sample_sentence1)
    print(f"Original: {sample_sentence1}, Reversed: {reversed_sentence1}")
    sample_sentence2 = "jumps over the lazy dog"
    reversed_sentence2 = reverser.reverse_words(sample_sentence2)
    print(f"Original: {sample_sentence2}, Reversed: {reversed_sentence2}")
    sample_sentence3 = "Python programming is fun"
    reversed_sentence3 = reverser.reverse_words(sample_sentence3)
    print(f"Original: {sample_sentence3}, Reversed: {reversed_sentence3}")