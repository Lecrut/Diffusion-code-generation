def word_generator(text):
    words = text.split()
    for word in words:
        cleaned_word = ""
        for char in word:
            if char.isalnum():
                cleaned_word += char
        if cleaned_word:
            yield cleaned_word
if __name__ == '__main__':
    sample_string = "Hello, world! This is a test string with some - punctuation and numbers 123."
    generator = word_generator(sample_string)
    for word in generator:
        print(word)