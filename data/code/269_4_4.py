def punctuation_generator(text):
    for char in text:
        if char in '.,!?;:"\'()[]{}':
            yield char
if __name__ == '__main__':
    sample_string = "Hello world! How are you, and how are you doing? Let's test this: \"It's fun.\""
    generator = punctuation_generator(sample_string)
    result = list(generator)
    print(result)