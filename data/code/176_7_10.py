def parse_paragraph(paragraph):
    words = paragraph.split()
    distinct_words = set(words)
    sorted_words = sorted(distinct_words)
    return sorted_words

if __name__ == '__main__':
    sample_paragraph = "This is a sample paragraph with some repeated words and some unique ones."
    result = parse_paragraph(sample_paragraph)
    print(result)