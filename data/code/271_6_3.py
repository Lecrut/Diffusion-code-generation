def longest_word(sentence):
    words = sentence.split()
    if not words:
        return ""
    longest = words[0]
    for word in words[1:]:
        if len(word) > len(longest):
            longest = word
    return longest

if __name__ == '__main__':
    sample_sentence = "The quick brown fox jumps over the lazy dog"
    print(longest_word(sample_sentence))