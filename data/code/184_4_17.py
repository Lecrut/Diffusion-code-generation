def check_word_presence(words_tuple, target_word):
    return any(word == target_word for word in words_tuple)

if __name__ == '__main__':
    sample_words = ('apple', 'banana', 'cherry')
    target = 'banana'
    print(check_word_presence(sample_words, target))