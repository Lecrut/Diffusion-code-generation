class SentenceReverser:
    @staticmethod
    def reverse_sentence(sentence):
        words = sentence.split()
        reversed_words = [word for word in reversed(words)]
        return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Implementing a class-based solution"
    reversed_sentence = SentenceReverser.reverse_sentence(sample_sentence)
    print(reversed_sentence)