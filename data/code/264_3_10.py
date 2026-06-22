def find_duplicate_words(text):
    words = text.split()
    word_count = {}
    duplicates = []

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for word, count in word_count.items():
        if count > 1:
            duplicates.append(word)

    return duplicates

if __name__ == '__main__':
    sample_text = "apple banana apple orange banana grape"
    print(find_duplicate_words(sample_text))