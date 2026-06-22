class WordChecker:
    def check_length(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return False
        return len(text.strip()) > 20

if __name__ == '__main__':
    checker = WordChecker()
    sample1 = "This is a short sentence"
    sample2 = "This is a very long sentence that definitely exceeds twenty characters"
    sample3 = ""
    sample4 = 12345
    print(f"'{sample1}' is long: {checker.check_length(sample1)}")
    print(f"'{sample2}' is long: {checker.check_length(sample2)}")
    print(f"'{sample3}' is long: {checker.check_length(sample3)}")
    print(f"'{sample4}' is long: {checker.check_length(sample4)}")