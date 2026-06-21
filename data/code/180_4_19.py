class WordSearcher:
    @staticmethod
    def contains_word(word_list, text):
        text_words = set(text.lower().split())
        return any(word.lower() in text_words for word in word_list)

if __name__ == '__main__':
    sample_word_list = ["apple", "banana", "cherry", "date"]
    sample_text = "This is a sentence about apples and bananas. Dates are sweet."
    result = WordSearcher.contains_word(sample_word_list, sample_text)
    print(result)