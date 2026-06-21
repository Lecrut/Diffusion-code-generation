def reverse_words_iterative(text):
    words = text.split()
    reversed_words = []
    for word in words:
        reversed_words.insert(0, word)
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_text = "Hello world from Python"
    print(reverse_words_iterative(sample_text))