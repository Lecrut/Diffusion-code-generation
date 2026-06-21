def is_word_present(words_set, word):
    return word.lower() in words_set

if __name__ == '__main__':
    words_list = ["Hello", "World", "Python", "Programming", "Case", "Sensitivity", "Test"]
    words_set = set(word.lower() for word in words_list)
    
    word_to_check1 = "world"
    print(f"'{word_to_check1}' in words: {is_word_present(words_set, word_to_check1)}")
    
    word_to_check2 = "python"
    print(f"'{word_to_check2}' in words: {is_word_present(words_set, word_to_check2)}")
    
    word_to_check3 = "case"
    print(f"'{word_to_check3}' in words: {is_word_present(words_set, word_to_check3)}")
    
    word_to_check4 = "match"
    print(f"'{word_to_check4}' in words: {is_word_present(words_set, word_to_check4)}")