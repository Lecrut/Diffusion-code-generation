def find_most_frequent_word(text):
    words = text.split()
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return max(word_frequency.items(), key=lambda item: item[1])

if __name__ == '__main__':
    sample_text = "python programming is fun and exciting"
    most_frequent, count = find_most_frequent_word(sample_text)
    print(f"The most frequent word is '{most_frequent}' with a count of {count}")