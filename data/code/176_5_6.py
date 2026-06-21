def word_generator(text):
    import re
    words = re.findall(r'\b\w+\b', text)
    for word in words:
        yield word

if __name__ == '__main__':
    large_string = "Hello, this is a test. It contains multiple   types of whitespace.\nAnd some punctuation!"
    gen = word_generator(large_string)
    print(next(gen))
    print(next(gen))
    print(next(gen))