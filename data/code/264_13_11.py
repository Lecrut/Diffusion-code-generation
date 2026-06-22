def count_words(text):
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def most_frequent_word(text):
    word_counts = count_words(text)
    if not word_counts:
        return None, 0
    most_frequent = max(word_counts.items(), key=lambda x: x[1])
    return most_frequent

if __name__ == '__main__':
    sample_text = "hello world hello python programming is fun and exciting"
    most_frequent, count = most_frequent_word(sample_text)
    print(f"The most frequent word is '{most_frequent}' with a count of {count}")