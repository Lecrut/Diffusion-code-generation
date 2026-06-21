class WordReverser:
    DELIMITER = ' '

    @staticmethod
    def reverse_sentence(sentence):
        if not isinstance(sentence, str):
            raise ValueError("Input must be a string")
        words = sentence.split(WordReverser.DELIMITER)
        reversed_words = words[::-1]
        return WordReverser.DELIMITER.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Hello world this is a test"
    reversed_sentence = WordReverser.reverse_sentence(sample_sentence)
    print(reversed_sentence)