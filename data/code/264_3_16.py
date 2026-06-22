def find_duplicate_words(text):
    tokens = text.split()
    word_count = {}
    
    for token in tokens:
        if token in word_count:
            word_count[token] += 1
        else:
            word_count[token] = 1
    
    duplicates = [word for word, count in word_count.items() if count > 1]
    return duplicates

if __name__ == '__main__':
    sample_text = "This is a large block of text that needs to be processed efficiently. Short words like 'a', 'is', and 'of' should be removed. Performance matters greatly."
    result = find_duplicate_words(sample_text)
    print(result)