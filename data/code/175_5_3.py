def word_generator(text):
    words = text.split()
    for word in words:
        cleaned_word = word.strip('.,?!:;"\'()[]{}')
        if cleaned_word:
            yield cleaned_word
if __name__ == '__main__':
    sample_string = "Hello, world! This is a test sentence, isn't it?"
    generator = word_generator(sample_string)
    for word in generator:
        print(word)