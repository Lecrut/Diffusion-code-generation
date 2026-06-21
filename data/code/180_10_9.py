class WordSearch:
    @staticmethod
    def create_word_set(words):
        return set(word.lower() for word in words)

    @staticmethod
    def is_word_present(word_set, word):
        return word.lower() in word_set

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    word_set = WordSearch.create_word_set(sample_words)
    
    search_word1 = "Banana"
    print(f"'{search_word1}' in words: {WordSearch.is_word_present(word_set, search_word1)}")
    
    search_word2 = "Grape"
    print(f"'{search_word2}' in words: {WordSearch.is_word_present(word_set, search_word2)}")