def parse_paragraph(paragraph):
    words = paragraph.split()
    distinct_words = sorted(set(words))
    return distinct_words

if __name__ == '__main__':
    sample_paragraph = "Another example with unique words and repeated ones. Let's see if it works."
    result = parse_paragraph(sample_paragraph)
    print(result)