class WordChecker:
    def __init__(self, word_list):
        self.word_set = set(word.lower() for word in word_list)

    def check_presence(self, text):
        return any(word in self.word_set for word in text.lower().split())

if __name__ == '__main__':
    checker = WordChecker(["apple", "banana", "cherry", "date"])
    sample_text = "This is a sentence about apples and bananas. Dates are sweet."
    result = checker.check_presence(sample_text)
    print(result)