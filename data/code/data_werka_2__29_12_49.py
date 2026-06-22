class WordReverser:
    @staticmethod
    def reverse(word):
        reversed_chars = []
        index = len(word) - 1
        while index >= 0:
            reversed_chars.append(word[index])
            index -= 1
        return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_word = "python"
    print(WordReverser.reverse(sample_word))