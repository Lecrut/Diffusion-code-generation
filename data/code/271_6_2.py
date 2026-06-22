def find_longest_word(sentence):
    words = sentence.split()
    longest_word = ""
    max_length = 0

    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)

    return longest_word

if __name__ == '__main__':
    sample_sentence = "A quick brown fox jumps over the lazy dog"
    print(find_longest_word(sample_sentence))