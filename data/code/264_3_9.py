def find_repeated_words(text):
    words = text.split()
    word_count = {}
    repeated_words = []

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for word, count in word_count.items():
        if count > 1:
            repeated_words.append(word)

    return repeated_words

if __name__ == '__main__':
    sample_text = "apple banana apple orange banana grape"
    print(find_repeated_words(sample_text))