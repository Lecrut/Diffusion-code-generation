def get_longest_word(sentence):
    words = sentence.split()
    if not words:
        return ""
    longest_word = words[0]
    max_length = len(longest_word)
    for word in words[1:]:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    return longest_word

if __name__ == '__main__':
    sample_sentence = "The quick brown fox jumps over the lazy dog"
    print(get_longest_word(sample_sentence))