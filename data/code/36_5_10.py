def reverse_string_generator(input_string):
    for char in reversed(input_string):
        yield char
if __name__ == '__main__':
    sample_string = "hello world"
    reversed_chars = reverse_string_generator(sample_string)
    result = list(reversed_chars)
    print(result)
    large_string = "abcdefghijklmnopqrstuvwxyz" * 10000
    reversed_large_chars = reverse_string_generator(large_string)
    result_large = list(reversed_large_chars)
    print(result_large[:10])