def is_word_long(word):
    if not isinstance(word, str) or word == "":
        return False
    return len(word) > 20

if __name__ == '__main__':
    sample1 = "This is a short sentence"
    sample2 = "This is a very long sentence that definitely exceeds twenty characters"
    sample3 = "Exactly twenty characters"
    
    print(f"'{sample1}': {is_word_long(sample1)}")
    print(f"'{sample2}': {is_word_long(sample2)}")
    print(f"'{sample3}': {is_word_long(sample3)}")