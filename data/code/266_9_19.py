def count_word_lengths(text):
    word_lengths = {}
    words = re.findall(r'\b\w+\b', text)
    for word in words:
        length = len(word)
        if length in word_lengths:
            word_lengths[length] += 1
        else:
            word_lengths[length] = 1
    return word_lengths

if __name__ == '__main__':
    sample_text = "Hello world! This is a test, how are you? One-two three... four five. Hyphenated-words should be counted as one if possible."
    result = count_word_lengths(sample_text)
    print(result)