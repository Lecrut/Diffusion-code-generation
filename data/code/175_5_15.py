def word_generator(text):
    for chunk in text.split():
        cleaned_chunk = chunk.strip('.,!?;:"\'()[]{}')
        if cleaned_chunk:
            yield from cleaned_chunk.split()

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test sentence with punctuation."
    word_gen = word_generator(sample_string)
    for word in word_gen:
        print(word)