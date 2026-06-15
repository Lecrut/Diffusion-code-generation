def word_stripper(text):
    words = text.split()
    for word in words:
        stripped_word = word.strip('.,!?;:"\'()[]{}')
        if stripped_word:
            yield stripped_word
if __name__ == '__main__':
    sample_string = "Hello, world! This is a test sentence... How are you?"
    for word in word_stripper(sample_string):
        print(word)