def invert_word_order(text):
    words = text.split()
    reversed_words = []
    for word in words:
        reversed_words.insert(0, word)
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_text = "Python is fun to learn"
    print(invert_word_order(sample_text))