def most_frequent_word(text):
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return max(word_count.items(), key=lambda x: x[1])

if __name__ == '__main__':
    sample_text = "the quick brown fox jumps over the lazy dog the"
    most_frequent, count = most_frequent_word(sample_text)
    print(f"The most frequent word is '{most_frequent}' with a count of {count}")