def reverse_words(text):
    words = text.split()
    return ' '.join(reversed(words))

if __name__ == '__main__':
    sample_text = "Hello world from Python"
    print(reverse_words(sample_text))