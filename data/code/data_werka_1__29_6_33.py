class WordReverser:
    @staticmethod
    def reverse(word):
        return word[::-1]

if __name__ == '__main__':
    sample_word = "hello"
    reversed_word = WordReverser.reverse(sample_word)
    print(reversed_word)