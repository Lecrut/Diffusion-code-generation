def word_generator(text):
    words = text.split()
    for word in words:
        stripped_word = word.strip('.,!?;:"\'()[]{}')
        if stripped_word:
            yield stripped_word
if __name__ == '__main__':
    sample_string = "Hello, world! This is a test sentence with punctuation."
    word_gen = word_generator(sample_string)
    result_list = list(word_gen)
    print(result_list)