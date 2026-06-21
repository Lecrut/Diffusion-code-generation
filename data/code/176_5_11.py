def word_generator(text):
    import re
    words = re.findall(r'\b\w+\b', text)
    for word in words:
        yield word

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test. 12345."
    gen = word_generator(sample_text)
    for _ in range(6):
        print(next(gen))