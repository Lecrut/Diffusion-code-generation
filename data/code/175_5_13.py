import re
PUNCTUATION = '.,!?;:"\'()[]{}'

def word_generator(text):
    for word in re.findall('\\b\\w+\\b', text):
        cleaned_word = word.strip(PUNCTUATION)
        if cleaned_word:
            yield cleaned_word
if __name__ == '__main__':
    sample_string = 'Hello, world! This is a test sentence with punctuation.'
    word_gen = word_generator(sample_string)
    for word in word_gen:
        print(word)