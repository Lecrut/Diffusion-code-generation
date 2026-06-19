def reverse_string_generator(input_string):
    for char in reversed(input_string):
        yield char

if __name__ == '__main__':
    sample_string = "Hello, World!"
    reversed_chars = reverse_string_generator(sample_string)
    print(''.join(reversed_chars))