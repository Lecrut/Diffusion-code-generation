class WordChecker:
    @staticmethod
    def check_word_presence(text, word):
        return word.lower() in text.lower()

if __name__ == '__main__':
    sample_string = "This is a Test String for checking the word test."
    sample_word_present = "Test"
    sample_word_absent = "missing"
    
    checker = WordChecker()
    result1 = checker.check_word_presence(sample_string, sample_word_present)
    result2 = checker.check_word_presence(sample_string, sample_word_absent)
    
    print(f"'{sample_word_present}' in '{sample_string}': {result1}")
    print(f"'{sample_word_absent}' in '{sample_string}': {result2}")