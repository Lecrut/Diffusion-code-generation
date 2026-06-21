def word_frequency(words):
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    sample_words = ["apple", "banana", "apple", "orange", "banana", "grape"]
    print(word_frequency(sample_words))