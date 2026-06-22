class WordEvaluator:
    def is_long(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return False
        return len(text) > 20

if __name__ == '__main__':
    evaluator = WordEvaluator()
    sample1 = "This is a short sentence"
    sample2 = "This is a very long sentence that definitely exceeds twenty characters"
    sample3 = ""
    sample4 = 123
    print(f"'{sample1}' is long: {evaluator.is_long(sample1)}")
    print(f"'{sample2}' is long: {evaluator.is_long(sample2)}")
    print(f"'{sample3}' is long: {evaluator.is_long(sample3)}")
    print(f"{sample4} is long: {evaluator.is_long(sample4)}")