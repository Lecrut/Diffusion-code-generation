class WordReverser:
    def reverse_words(self, s):
        return ' '.join(s.split()[::-1])

if __name__ == '__main__':
    reverser = WordReverser()
    sample_string = "The quick brown fox"
    print(reverser.reverse_words(sample_string))