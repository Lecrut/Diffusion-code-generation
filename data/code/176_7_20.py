def parse_and_sort_words(paragraph):
    words = paragraph.split()
    distinct_words = sorted(set(words))
    return distinct_words

if __name__ == '__main__':
    sample_paragraph = "This is a sample paragraph with some repeated words and some unique ones."
    result = parse_and_sort_words(sample_paragraph)
    print(result)