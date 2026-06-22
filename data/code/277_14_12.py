WORD_DELIMITER = ' '

def count_words(text):
    words = text.split(WORD_DELIMITER)
    return len(words)
if __name__ == '__main__':
    sample_text = 'Hello world this is a test'
    print(count_words(sample_text))