def parse_and_sort_paragraph(paragraph):
    words = paragraph.split()
    distinct_words = sorted(set(words))
    return distinct_words

if __name__ == '__main__':
    sample_paragraph = "Hello world. Welcome to the world of Python programming."
    result = parse_and_sort_paragraph(sample_paragraph)
    print(result)