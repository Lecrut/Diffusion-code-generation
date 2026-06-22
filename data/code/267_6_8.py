class WordAnalyzer:
    MIN_LENGTH = 10

    @staticmethod
    def is_long(word):
        return len(word) > WordAnalyzer.MIN_LENGTH

if __name__ == '__main__':
    words_to_check = ["short", "thisisalongword", "anotherword", "verylongwordexample"]
    for word in words_to_check:
        print(f"Word: {word}, Is Long: {WordAnalyzer.is_long(word)}")