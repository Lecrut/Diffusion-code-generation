def word_frequency(text):
    WORD_DELIMITERS = " \t\n.,;:!?"
    words = text.lower().split(WORD_DELIMITERS)
    frequency = {}
    for word in words:
        if word:
            frequency[word] = frequency.get(word, 0) + 1
    return frequency

if __name__ == '__main__':
    sample_text = "Hello world hello Python python"
    result = word_frequency(sample_text)
    print(result)