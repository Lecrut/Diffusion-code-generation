def count_words(paragraph):
    words = paragraph.split()
    return len(words)

if __name__ == '__main__':
    sample_paragraph = "Hello world! This is a test paragraph."
    print(count_words(sample_paragraph))