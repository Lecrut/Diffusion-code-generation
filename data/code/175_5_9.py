def word_generator(text):
    words = text.split()
    for word in words:
        cleaned_word = word.strip('.,!?;:"\'()[]{}')
        if cleaned_word:
            yield cleaned_word

if __name__ == '__main__':
    sample_string = "Python is an interpreted, high-level and general-purpose programming language."
    word_gen = word_generator(sample_string)
    result_list = list(word_gen)
    print(result_list)