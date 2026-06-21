def is_word_present(word_set, word):
    return word.lower() in word_set

if __name__ == '__main__':
    words = set(["apple", "banana", "cherry", "date"])
    search_word1 = "Banana"
    print(f"'{search_word1}' in set: {is_word_present(words, search_word1)}")
    search_word2 = "grape"
    print(f"'{search_word2}' in set: {is_word_present(words, search_word2)}")