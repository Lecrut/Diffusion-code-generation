def word_generator(text):
    chunks = text.split()
    for chunk in chunks:
        yield chunk.strip('.,!?;:"\'()[]{}')

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test sentence with punctuation."
    gen = word_generator(sample_string)
    print(next(gen))
    print(next(gen))