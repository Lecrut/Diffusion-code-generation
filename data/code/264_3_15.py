def find_duplicate_words(text):
    words = text.split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    duplicates = [word for word, count in word_count.items() if count > 1]
    return duplicates

if __name__ == '__main__':
    sample_text = "This is a sample text with some words that are repeated. Repeated words will be found and listed."
    result = find_duplicate_words(sample_text)
    print(result)