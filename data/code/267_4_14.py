class WordEvaluator:
    MIN_LENGTH = 10

    @staticmethod
    def is_long_word(word):
        return len(word) > WordEvaluator.MIN_LENGTH

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    for word in sample_words:
        print(f"The word '{word}' is long: {WordEvaluator.is_long_word(word)}")