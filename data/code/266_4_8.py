def count_unique_words(text):
    word_counts = {}
    for word in text.split():
        if word not in word_counts:
            word_counts[word] = 1
    return len(word_counts)

if __name__ == '__main__':
    sample_text = "hello world hello Python"
    print(count_unique_words(sample_text))