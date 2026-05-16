def reverse_string_generator(input_string):
    for char in reversed(input_string):
        yield char
if __name__ == '__main__':
    sample_string = "Hello World"
    reversed_chars = reverse_string_generator(sample_string)
    result = list(reversed_chars)
    print(result)
    sample_string_large = "This is a very long string for testing memory efficiency"
    reversed_chars_large = reverse_string_generator(sample_string_large)
    result_large = list(reversed_chars_large)
    print(result_large)