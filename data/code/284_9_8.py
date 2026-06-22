class WordReverser:
    def reverse_words(self, s):
        return ' '.join(word[::-1] for word in s.split())

if __name__ == '__main__':
    reverser = WordReverser()
    sample_string = "Hello world from Python"
    print(reverser.reverse_words(sample_string))