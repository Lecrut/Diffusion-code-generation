def reverse_words_in_string(input_string):
    return ' '.join(word[::-1] for word in input_string.split())

if __name__ == '__main__':
    sample_input = "Hello world from Python"
    print(reverse_words_in_string(sample_input))