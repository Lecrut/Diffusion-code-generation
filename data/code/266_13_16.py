def count_words(paragraph):
    words = paragraph.split()
    return len(words)

if __name__ == '__main__':
    sample_paragraph = "Hello world! This is a test paragraph."
    word_count = count_words(sample_paragraph)
    print(word_count)