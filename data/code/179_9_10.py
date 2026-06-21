def invert_word_order(text):
    words = text.split()
    reversed_words = []
    for word in reversed(words):
        reversed_words.append(word)
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_text = "Hello world from Python"
    print(invert_word_order(sample_text))