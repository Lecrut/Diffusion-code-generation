def word_generator(text):
    import re
    words = re.findall(r'\b\w+\b', text)
    for word in words:
        yield word

if __name__ == '__main__':
    sample_text = "Hello, this is a test. It contains various types of whitespace: tabs\tand newlines\n."
    gen = word_generator(sample_text)
    print(next(gen))
    print(next(gen))
    print(next(gen))