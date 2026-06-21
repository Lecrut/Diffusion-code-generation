def word_exists(word_set, search_word):
    return search_word in word_set

if __name__ == '__main__':
    sample_words = {"apple", "banana", "cherry", "date"}
    search_term = "banana"
    
    if not isinstance(sample_words, set) or not all(isinstance(item, str) for item in sample_words):
        raise ValueError("sample_words must be a set of strings")
    if not isinstance(search_term, str):
        raise ValueError("search_term must be a string")
    
    result = word_exists(sample_words, search_term)
    print(result)