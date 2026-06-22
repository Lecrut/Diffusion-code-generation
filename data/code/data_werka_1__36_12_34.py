class WordReverser:
    def reverse(self, sentence):
        words = sentence.split()
        reversed_words = ' '.join(words[::-1])
        return reversed_words

if __name__ == '__main__':
    reverser = WordReverser()
    sample_sentence_1 = "The quick brown fox"
    reversed_sentence_1 = reverser.reverse(sample_sentence_1)
    print(f"Original: {sample_sentence_1}, Reversed: {reversed_sentence_1}")
    
    sample_sentence_2 = "jumps over the lazy dog"
    reversed_sentence_2 = reverser.reverse(sample_sentence_2)
    print(f"Original: {sample_sentence_2}, Reversed: {reversed_sentence_2}")
    
    sample_sentence_3 = "Python programming is fun"
    reversed_sentence_3 = reverser.reverse(sample_sentence_3)
    print(f"Original: {sample_sentence_3}, Reversed: {reversed_sentence_3}")