def word_generator(text):
    for chunk in text.split():
        yield chunk.strip('.,!?;:"\'()[]{}')

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test sentence with punctuation."
    word_gen = word_generator(sample_string)
    result_list = list(word_gen)
    print(result_list)