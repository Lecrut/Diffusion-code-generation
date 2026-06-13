def word_generator(text):
    words = text.split()
    for word in words:
        filtered_word = ""
        for char in word:
            if char.isalnum():
                filtered_word += char
        if filtered_word:
            yield filtered_word
if __name__ == '__main__':
    sample_string = "Hello, world! This is a test... with some symbols 123."
    generator = word_generator(sample_string)
    result = list(generator)
    print(result)