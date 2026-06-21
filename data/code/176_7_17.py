def extract_words(paragraph):
    words = paragraph.split()
    return [word.lower() for word in words if word.isalpha()]

def parse_paragraph(paragraph):
    words = extract_words(paragraph)
    distinct_words = sorted(set(words))
    return distinct_words

if __name__ == '__main__':
    sample_paragraph = "This is a sample paragraph with some repeated words. This is just for demonstration."
    result = parse_paragraph(sample_paragraph)
    print(result)