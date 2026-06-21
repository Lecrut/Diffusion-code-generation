class WordSearch:
    @staticmethod
    def contains_word(words_tuple, target_word):
        return any(target_word in word for word in words_tuple)

if __name__ == '__main__':
    sample_words = ("apple", "banana", "cherry")
    search_term = "banana"
    result = WordSearch.contains_word(sample_words, search_term)
    print(result)