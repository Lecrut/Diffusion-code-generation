def invert_word_order(text):
    return ' '.join(text.split()[::-1])

if __name__ == '__main__':
    sample_text = "Hello world from Python"
    print(invert_word_order(sample_text))