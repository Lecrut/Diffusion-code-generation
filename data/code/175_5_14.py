def word_generator(text):
    words = text.split()
    for word in words:
        cleaned_word = word.strip('.,!?;:"\'()[]{}')
        if cleaned_word:
            yield cleaned_word

if __name__ == '__main__':
    sample_string = "Good morning! How are you today? Have a great day!"
    word_gen = word_generator(sample_string)
    for word in word_gen:
        print(word)