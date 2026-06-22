def count_word_lengths(text):
    words = text.split()
    length_count = {}
    for word in words:
        length = len(word)
        if length in length_count:
            length_count[length] += 1
        else:
            length_count[length] = 1
    return length_count
if __name__ == '__main__':
    sample_text = 'The quick brown fox jumps over the lazy dog.'
    result = count_word_lengths(sample_text)
    print(result)