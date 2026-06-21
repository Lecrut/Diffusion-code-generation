def parse_and_sort_words(paragraph):
    words = paragraph.split()
    distinct_words = sorted(set(words))
    return distinct_words

if __name__ == '__main__':
    sample_paragraph = "Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace."
    result = parse_and_sort_words(sample_paragraph)
    print(result)