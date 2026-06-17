class WordChecker:
    def check_length(self, text):
        return len(text) > 20
if __name__ == '__main__':
    checker = WordChecker()
    sample1 = "This is a short sentence"
    sample2 = "This is a very long sentence that definitely exceeds twenty characters"
    sample3 = "Exactly twenty characters"
    print(f"'{sample1}' is long: {checker.check_length(sample1)}")
    print(f"'{sample2}' is long: {checker.check_length(sample2)}")
    print(f"'{sample3}' is long: {checker.check_length(sample3)}")