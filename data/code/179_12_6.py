def reverse_word_order(text):
    return ' '.join(reversed(text.split()))

if __name__ == '__main__':
    sample_text = "Hello world from Python"
    print(reverse_word_order(sample_text))