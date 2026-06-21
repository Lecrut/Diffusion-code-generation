def word_generator(text):
    start = 0
    while start < len(text):
        end = start
        while end < len(text) and text[end].isspace():
            end += 1
        if end > start:
            yield text[start:end]
        start = end + 1

if __name__ == '__main__':
    sample_text = "Hello,   world! This is a test."
    for word in word_generator(sample_text):
        print(word)