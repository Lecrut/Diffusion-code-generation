def is_word_in_list(word_list, word):
    return word.lower() in {item.lower() for item in word_list}

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    search_word1 = "Banana"
    print(f"'{search_word1}' in list: {is_word_in_list(sample_list, search_word1)}")
    
    search_word2 = "orange"
    print(f"'{search_word2}' in list: {is_word_in_list(sample_list, search_word2)}")