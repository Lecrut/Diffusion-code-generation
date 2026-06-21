def count_word_frequency(words):
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return sorted(frequency.items(), key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    sample_words = ["apple", "banana", "apple", "orange", "banana", "apple"]
    word_freq = count_word_frequency(sample_words)
    print(word_freq)