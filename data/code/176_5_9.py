def word_generator(text):
    import re
    words = re.findall('\\b\\w+\\b', text)
    for word in words:
        yield word
if __name__ == '__main__':
    sample_text = 'Hello, world! This is a test. 123.'
    gen = word_generator(sample_text)
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))