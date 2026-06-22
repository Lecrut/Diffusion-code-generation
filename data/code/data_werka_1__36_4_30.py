def reverse_string_generator(s):
    for char in reversed(s):
        yield char

if __name__ == '__main__':
    sample_string = "Hello, World!"
    reversed_chars = reverse_string_generator(sample_string)
    for char in reversed_chars:
        print(char, end='')