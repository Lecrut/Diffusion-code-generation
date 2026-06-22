class WordEvaluator:
    MIN_LENGTH = 10

    @staticmethod
    def is_long(word):
        return len(word) > WordEvaluator.MIN_LENGTH

if __name__ == '__main__':
    words_to_check = ["short", "thisiswaylong", "exactlytwelve"]
    for word in words_to_check:
        print(f"The word '{word}' is long: {WordEvaluator.is_long(word)}")