def find_repeated_words(text):
    words = text.lower().split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    repeated_words = [word for word, count in word_count.items() if count > 1]
    return repeated_words
if __name__ == '__main__':
    sample_text = "This is a large block of text that needs to be processed efficiently. Short words like 'a', 'is', and 'of' should be removed. Performance matters greatly."
    result = find_repeated_words(sample_text)
    print(result)