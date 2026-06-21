def reverse_words(text):
    words = text.split()
    reversed_text = ' '.join(reversed(words))
    return reversed_text

if __name__ == '__main__':
    sample_text = "Hello world from Python"
    print(reverse_words(sample_text))