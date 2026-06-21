def reverse_words(input_string):
    return ' '.join(reversed(input_string.split()))

if __name__ == '__main__':
    sample_input = "hello world from Python"
    print(reverse_words(sample_input))