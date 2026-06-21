def count_word_frequency(words):
    if not isinstance(words, list) or not all(isinstance(word, str) for word in words):
        raise ValueError("Input must be a list of strings")
    
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return sorted(frequency.items(), key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    sample_words = ["apple", "banana", "apple", "orange", "banana", "apple"]
    result = count_word_frequency(sample_words)
    print(result)