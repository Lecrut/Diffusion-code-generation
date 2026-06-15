def word_frequency(phrase):
    words = phrase.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency
if __name__ == '__main__':
    sample_phrase = "this is a sample phrase for testing"
    result = word_frequency(sample_phrase)
    print(result)