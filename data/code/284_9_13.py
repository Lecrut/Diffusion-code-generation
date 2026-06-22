class WordReverser:
    @staticmethod
    def reverse_words_in_string(s):
        return ' '.join(word[::-1] for word in s.split())

if __name__ == '__main__':
    sample_input = "Python is fun to learn"
    result = WordReverser.reverse_words_in_string(sample_input)
    print(result)