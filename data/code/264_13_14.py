def count_words(text):
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def most_frequent_word(word_count):
    return max(word_count.items(), key=lambda x: x[1])

if __name__ == '__main__':
    sample_text = "hello world hello python programming is fun and exciting"
    word_count = count_words(sample_text)
    most_frequent, count = most_frequent_word(word_count)
    print(f"The most frequent word is '{most_frequent}' with a count of {count}")