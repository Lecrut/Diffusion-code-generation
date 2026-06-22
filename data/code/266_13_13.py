def count_words(paragraph):
    return len(paragraph.split())

if __name__ == '__main__':
    sample_paragraph = "This is a sample paragraph to test the word counting function."
    print(count_words(sample_paragraph))