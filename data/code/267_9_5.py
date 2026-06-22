class WordEvaluator:
    def __init__(self, min_length=6):
        self.min_length = min_length

    def is_word_long(self, word):
        return len(word) > self.min_length

if __name__ == '__main__':
    evaluator = WordEvaluator(min_length=7)
    
    words_to_test = [
        "short",
        "thisisalongstring",
        "onlyletters",
        "this has a space",
        "abcdefghij",
        "a" * 11,
        "1234567890"
    ]
    
    for word in words_to_test:
        result = evaluator.is_word_long(word)
        print(f"Input: '{word}', Result: {result}")