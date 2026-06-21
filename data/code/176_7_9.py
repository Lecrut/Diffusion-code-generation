def extract_words(paragraph):
    return paragraph.split()

def filter_unique(words):
    return sorted(set(words))

def parse_paragraph(paragraph):
    words = extract_words(paragraph)
    distinct_words = filter_unique(words)
    return distinct_words

if __name__ == '__main__':
    sample_paragraph = "This is a sample paragraph with some repeated words. This is just for demonstration."
    result = parse_paragraph(sample_paragraph)
    print(result)