def count_word_frequency(words):
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

if __name__ == '__main__':
    sample_words = ["apple", "banana", "apple", "orange", "banana", "grape"]
    result = count_word_frequency(sample_words)
    sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    print(sorted_result)