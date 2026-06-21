def word_generator(text):
    word = []
    for char in text:
        if char.isalpha():
            word.append(char)
        elif word:
            yield ''.join(word)
            word.clear()
    if word:
        yield ''.join(word)

if __name__ == '__main__':
    sample_string = "Hello world! This is a test, with 123 numbers and symbols like @#$"
    for word in word_generator(sample_string):
        print(word)