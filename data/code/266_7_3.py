def count_words(text):
    if not text:
        return 0
    words = text.split()
    return len(words)
if __name__ == '__main__':
    sample_string = "This is an example sentence for word counting optimization"
    word_count = count_words(sample_string)
    print(word_count)