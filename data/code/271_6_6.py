def longest_word(sentence):
    words = sentence.split()
    max_length = 0
    longest_word = ""
    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    return longest_word

if __name__ == '__main__':
    sample_sentence = "The quick brown fox jumps over the lazy dog"
    print(longest_word(sample_sentence))