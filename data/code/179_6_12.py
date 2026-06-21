def reverse_words(text):
    words = text.split()
    reversed_text = ' '.join(reversed(words))
    return reversed_text

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog"
    print(reverse_words(sample_text))