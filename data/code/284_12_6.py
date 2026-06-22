def reverse_words(input_string):
    words = input_string.split()
    return ' '.join(reversed(words))

if __name__ == '__main__':
    sample_input = "Hello world from Python"
    result = reverse_words(sample_input)
    print(result)