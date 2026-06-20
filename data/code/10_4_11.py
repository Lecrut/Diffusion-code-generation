def reverse_words(text):
    words = text.split()
    return ' '.join(reversed(words))

if __name__ == '__main__':
    sample_text = "Hello World from Python"
    result = reverse_words(sample_text)
    print(result)