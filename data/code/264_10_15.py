def word_frequency(text):
    words = text.lower().split()
    frequency = {}
    for word in words:
        if word not in frequency:
            frequency[word] = 0
        frequency[word] += 1
    return frequency

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog. The dog barked."
    result = word_frequency(sample_text)
    print(result)