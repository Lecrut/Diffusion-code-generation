def word_generator(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    words = text.split()
    for word in words:
        cleaned_word = word.strip('.,!?;:"\'()[]{}')
        if cleaned_word:
            yield cleaned_word

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test sentence... How are you?"
    try:
        word_gen = word_generator(sample_string)
        for word in word_gen:
            print(word)
    except ValueError as e:
        print(e)