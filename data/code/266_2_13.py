def count_word_frequency(text):
    word_count = {}
    words = text.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

if __name__ == '__main__':
    sample_text = "Hello world hello Python programming. Programming is fun!"
    result = count_word_frequency(sample_text)
    print(f"Word Frequency: {result}")