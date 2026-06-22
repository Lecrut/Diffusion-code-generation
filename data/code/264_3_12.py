def find_repeated_words(text):
    words = text.lower().split()
    word_count = {}
    repeated_words = set()

    for word in words:
        if word in word_count:
            repeated_words.add(word)
        else:
            word_count[word] = 1

    return list(repeated_words)

if __name__ == '__main__':
    sample_text = "This is a large block of text that needs to be processed efficiently. Short words like 'a', 'is', and 'of' should be removed. Performance matters greatly."
    result = find_repeated_words(sample_text)
    print(result)