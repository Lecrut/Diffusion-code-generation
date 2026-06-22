def longest_word(sentence):
    words = sentence.split()
    if not words:
        return ""
    max_length = 0
    longest_word = ""
    for word in words:
        length = len(word)
        if length > max_length:
            max_length = length
            longest_word = word
    return longest_word

if __name__ == '__main__':
    sample_sentence = "The quick brown fox jumps over the lazy dog"
    print(longest_word(sample_sentence))