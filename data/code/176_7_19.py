def parse_paragraph(paragraph):
    if not isinstance(paragraph, str):
        raise ValueError("Input must be a string")
    
    words = paragraph.split()
    distinct_words = sorted(set(words))
    return distinct_words

if __name__ == '__main__':
    sample_paragraph = "This is a sample paragraph with some repeated words. This is just for demonstration."
    result = parse_paragraph(sample_paragraph)
    print(result)