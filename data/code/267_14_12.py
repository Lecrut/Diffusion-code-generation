def contains_long_word(word_list):
    for word in word_list:
        if len(word) > 7:
            return True
    return False

if __name__ == '__main__':
    sample_words = ["apple", "pineapple", "grape", "watermelon"]
    print(contains_long_word(sample_words))