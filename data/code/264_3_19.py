def find_duplicate_words(text):
    words = text.lower().split()
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
    sample_text = "This is a large block of text that needs to be processed efficiently. Short words like 'a', 'is', and 'of' should be removed. Performance matters greatly, but some words might repeat."
    result = find_duplicate_words(sample_text)
    print(result)