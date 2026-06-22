class WordEvaluator:
    MIN_LENGTH = 10

    @staticmethod
    def is_long_word(word):
        return len(word) > WordEvaluator.MIN_LENGTH

if __name__ == '__main__':
    evaluator = WordEvaluator()
    print(evaluator.is_long_word("short"))
    print(evaluator.is_long_word("thisiswaylong"))
    print(evaluator.is_long_word("exactlytwelve"))