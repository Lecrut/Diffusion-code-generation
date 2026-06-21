class WordReverser:
    @staticmethod
    def reverse_sentence(sentence):
        words = sentence.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "This is a sample sentence"
    result = WordReverser.reverse_sentence(sample_sentence)
    print(result)