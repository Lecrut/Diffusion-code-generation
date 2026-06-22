class WordEvaluator:

    def __init__(self, min_length=5):
        self.min_length = min_length

    def is_word_long(self, word):
        return len(word) > self.min_length
if __name__ == '__main__':
    evaluator = WordEvaluator(7)
    print(evaluator.is_word_long('hello'))
    print(evaluator.is_word_long('worldly'))
    print(evaluator.is_word_long('example'))
    print(evaluator.is_word_long('cat'))