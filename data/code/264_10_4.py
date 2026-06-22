def word_frequency(text):
    words = text.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

if __name__ == '__main__':
    sample_text = "Hello world hello Python python"
    result = word_frequency(sample_text)
    print(result)