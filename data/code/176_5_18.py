def word_generator(text):
    import re
    for match in re.finditer(r'\b\w+\b', text):
        yield match.group(0)

if __name__ == '__main__':
    sample_text = "Hello, this is a test. It contains various types of whitespace: tabs\tand newlines\n."
    generator = word_generator(sample_text)
    for _ in range(10):
        print(next(generator))