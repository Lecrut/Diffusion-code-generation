class WordChecker:
    @staticmethod
    def check_word_presence(word_list, text):
        text_words = set(text.lower().split())
        return any(word.lower() in text_words for word in word_list)

if __name__ == '__main__':
    sample_word_list = ["apple", "banana", "cherry", "date"]
    sample_text = "This is a sentence about apples and bananas. Dates are sweet."
    result = WordChecker.check_word_presence(sample_word_list, sample_text)
    print(result)