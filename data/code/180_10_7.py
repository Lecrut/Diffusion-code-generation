def is_word_present(word_list, word):
    if not isinstance(word_list, list) or not all(isinstance(item, str) for item in word_list):
        raise ValueError("word_list must be a list of strings")
    if not isinstance(word, str):
        raise ValueError("word must be a string")

    word_set = set(word.lower() for word in word_list)
    return word.lower() in word_set

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    sample_word1 = "Banana"
    print(f"'{sample_word1}' in {sample_list}: {is_word_present(sample_list, sample_word1)}")
    
    sample_word2 = "orange"
    print(f"'{sample_word2}' in {sample_list}: {is_word_present(sample_list, sample_word2)}")