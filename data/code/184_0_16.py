def word_exists(word_set, target_word):
    return target_word in word_set

if __name__ == '__main__':
    sample_words = {"apple", "banana", "cherry", "date"}
    target = "banana"
    print(word_exists(sample_words, target))