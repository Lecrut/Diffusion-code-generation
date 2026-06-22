def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest

if __name__ == '__main__':
    sample_sentence = "The quick brown fox jumps over the lazy dog"
    print(longest_word(sample_sentence))