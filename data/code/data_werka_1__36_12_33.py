class WordReverser:
    DELIMITER = ' '

    @staticmethod
    def reverse_words(sentence):
        words = sentence.split(WordReverser.DELIMITER)
        reversed_sentence = WordReverser.DELIMITER.join(words[::-1])
        return reversed_sentence

if __name__ == '__main__':
    sample_sentence1 = "The quick brown fox"
    reversed_sentence1 = WordReverser.reverse_words(sample_sentence1)
    print(f"Original: {sample_sentence1}, Reversed: {reversed_sentence1}")

    sample_sentence2 = "jumps over the lazy dog"
    reversed_sentence2 = WordReverser.reverse_words(sample_sentence2)
    print(f"Original: {sample_sentence2}, Reversed: {reversed_sentence2}")

    sample_sentence3 = "Python programming is fun"
    reversed_sentence3 = WordReverser.reverse_words(sample_sentence3)
    print(f"Original: {sample_sentence3}, Reversed: {reversed_sentence3}")