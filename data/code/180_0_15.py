class WordChecker:
    @staticmethod
    def check_word_presence(word_list, word):
        return word in set(word_list)

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    sample_word_present = "banana"
    sample_word_absent = "grape"

    checker = WordChecker()
    result1 = checker.check_word_presence(sample_words, sample_word_present)
    result2 = checker.check_word_presence(sample_words, sample_word_absent)

    print(f"Checking if '{sample_word_present}' is in the list: {result1}")
    print(f"Checking if '{sample_word_absent}' is in the list: {result2}")