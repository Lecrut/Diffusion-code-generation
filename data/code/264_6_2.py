def word_frequency(text):
    words = text.lower().split()
    frequency = {}
    for word in words:
        if word:
            frequency[word] = frequency.get(word, 0) + 1
    return frequency
if __name__ == '__main__':
    sample_text = "This is a sample sentence for word counting. This sentence has some repeated words."
    result = word_frequency(sample_text)
    print(result)