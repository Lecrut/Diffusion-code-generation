def check_word_in_tuple(word, word_tuple):
    return any(word in phrase for phrase in word_tuple)

if __name__ == '__main__':
    sample_word = "hello"
    sample_tuple = ("hi there", "how are you", "hello world")
    print(check_word_in_tuple(sample_word, sample_tuple))