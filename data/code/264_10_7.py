def word_frequency(text):
    words = text.lower().split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

if __name__ == '__main__':
    SAMPLE_TEXT = "Hello world hello Python python"
    print(word_frequency(SAMPLE_TEXT))