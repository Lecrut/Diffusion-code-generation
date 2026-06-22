def reverse_word_order(text):
    return ' '.join(reversed(text.split()))

if __name__ == '__main__':
    sample_string = "Hello world from Python"
    result = reverse_word_order(sample_string)
    print(result)