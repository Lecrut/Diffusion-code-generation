class WordProcessor:
    MAX_LENGTH = 1000

    @staticmethod
    def reverse(word):
        if not isinstance(word, str):
            raise ValueError("Input must be a string")
        if len(word) > WordProcessor.MAX_LENGTH:
            raise ValueError("Word length exceeds maximum allowed")
        return word[::-1]

if __name__ == '__main__':
    sample_word = "optimization"
    reversed_word = WordProcessor.reverse(sample_word)
    print(reversed_word)