def case_insensitive_match(search_word, word_list):
    lower_search_word = search_word.lower()
    return any(word.lower() == lower_search_word for word in word_list)

if __name__ == '__main__':
    sample_keyword = 'hello'
    sample_collection = ['Goodbye', 'Hello', 'WORLD']
    result = case_insensitive_match(sample_keyword, sample_collection)
    print(result)